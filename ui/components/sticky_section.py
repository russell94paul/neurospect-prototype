from nicegui import ui
from typing import Callable

def sticky_section(tabs: list[dict], on_tab_change: Callable[[int], None], default_index: int = 0):
    current_index = {"value": default_index}
    button_refs = []

    with ui.column().classes('w-full'):
        @ui.refreshable
        def tab_bar():
            button_refs.clear()

            # Sticky wrapper with spacing below nav bar
            with ui.column().classes('sticky top-[80px] z-50 px-0 pb-6'):
                with ui.element('div').classes('relative w-full'):
                    # 🟣 Fully rounded transparent background panel
                    ui.element('div').classes(
                        'absolute inset-0 bg-black bg-opacity-90 backdrop-blur border border-gray-800 z-[-1] rounded-xl'
                    )

                    # Label + Button row
                    with ui.column().classes('px-4 pt-2 pb-6'):
                        ui.label("📓 Journal Your Trade").classes("mt-2 text-xl font-bold text-purple-400 pl-2 pb-1")

                        with ui.row().classes('flex-wrap gap-2 items-center justify-center relative'):
                            for i, tab_data in enumerate(tabs):
                                label = tab_data["label"]
                                icon = tab_data.get("icon", "")
                                is_active = current_index["value"] == i

                                def make_click_handler(index=i):
                                    def on_click():
                                        current_index["value"] = index
                                        on_tab_change(index)
                                        tab_bar.refresh()
                                        ui.timer(0.05, lambda: move_indicator(index), once=True)
                                    return on_click

                                button = ui.button(on_click=make_click_handler()).props('flat data-tab').classes(
                                    'h-14 px-6 gap-2 text-nowrap text-white font-semibold rounded-xl shadow-md transition-all '
                                    'hover:scale-[1.02] shrink '
                                    + (
                                        'bg-gradient-to-br from-purple-500 to-blue-500'
                                        if is_active else
                                        'bg-gradient-to-br from-[#1f1f38] to-[#161627]'
                                    )
                                )

                                if icon:
                                    button.props(f'icon={icon}')
                                button.set_text(label)
                                button_refs.append(button)

                            # Purple animated underline indicator
                            ui.element('div').props('id=tab-indicator').classes(
                                'absolute bottom-0 h-1 bg-purple-500 rounded transition-all duration-300 ease-in-out'
                            )

        tab_bar()

        # Content section beneath sticky bar
        ui.column().classes('w-full px-4 py-4')
        on_tab_change(current_index["value"])

    def move_indicator(index: int):
        js = f"""
        const tab = document.querySelectorAll('[data-tab]')[{index}];
        const indicator = document.getElementById('tab-indicator');
        if (tab && indicator) {{
            const rect = tab.getBoundingClientRect();
            const parentRect = tab.parentElement.getBoundingClientRect();
            indicator.style.width = `${{rect.width}}px`;
            indicator.style.left = `${{rect.left - parentRect.left}}px`;
        }}
        """
        ui.run_javascript(js)

    # Position underline on load
    ui.timer(0.2, lambda: move_indicator(current_index["value"]), once=True)