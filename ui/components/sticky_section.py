from nicegui import ui
from typing import Callable

def sticky_section(tabs: list[dict], on_tab_change: Callable[[int], None], default_index: int = 0):
    current_index = {"value": default_index}
    button_refs = []

    # 🎨 Global styles and animations
    ui.add_head_html("""
    <style>
    @keyframes fadeInUp {
      0% { opacity: 0; transform: translateY(4px); }
      100% { opacity: 1; transform: translateY(0); }
    }

    .animate-fade-in-up {
      animation: fadeInUp 0.8s ease-out forwards;
    }

    .stagger-1 { animation-delay: 0.05s; }
    .stagger-2 { animation-delay: 0.12s; }
    .stagger-3 { animation-delay: 0.19s; }
    .stagger-4 { animation-delay: 0.26s; }
    .stagger-5 { animation-delay: 0.33s; }
    .stagger-6 { animation-delay: 0.40s; }
    .stagger-7 { animation-delay: 0.47s; }

    @keyframes bounceSubtle {
      0%   { transform: scale(1); }
      40%  { transform: scale(1.025); }
      100% { transform: scale(1); }
    }

    .bounce-selected {
      animation: bounceSubtle 300ms cubic-bezier(0.34, 1.56, 0.64, 1) forwards;
    }

    @keyframes fadeIn {
      from { opacity: 0; }
      to { opacity: 1; }
    }

    .animate-fade-in {
      animation: fadeIn 0.6s ease-in;
    }

    .glow-hover:hover {
      box-shadow: 0 0 8px rgba(168, 85, 247, 0.8);
      transform: scale(1.03);
    }
    </style>
    """)

    with ui.column().classes('w-full'):

        @ui.refreshable
        def tab_bar():
            button_refs.clear()

            with ui.column().classes('sticky top-[80px] z-50 px-0 pb-6'):
                with ui.element('div').classes('relative w-full'):

                    # 💠 Floating blurred tab panel
                    ui.element('div').classes(
                        'absolute inset-0 bg-black bg-opacity-90 backdrop-blur border border-gray-800 '
                        'z-[-1] rounded-xl shadow-xl ring-1 ring-white/10'
                    )

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
                                        tab_bar.refresh()
                                        render_tab(index)
                                        ui.timer(0.05, lambda: move_indicator(index), once=True)
                                    return on_click

                                # Entry cascade on first load
                                entry_animation = f'animate-fade-in-up stagger-{i+1}' if first_render["value"] else ''

                                # Bounce on click only for selected and nearby tabs
                                is_near = abs(i - current_index["value"]) <= 1
                                bounce_class = 'bounce-selected' if is_near and not first_render["value"] else ''

                                button = ui.button(on_click=make_click_handler()).props('flat data-tab').classes(
                                    f'h-14 px-6 gap-2 text-nowrap text-white font-semibold rounded-xl shadow-md '
                                    f'transition-all duration-300 shrink glow-hover {entry_animation} {bounce_class} '
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

                            # 🟪 Purple animated underline
                            ui.element('div').props('id=tab-indicator').classes(
                                'absolute bottom-0 h-1 bg-purple-500 rounded transition-all duration-300 ease-in-out'
                            )

        # Internal flag: only animate on first load
        first_render = {"value": True}
        tab_bar()
        first_render["value"] = False

        # 📦 Content container below tab bar
        content_area = ui.column().classes('w-full px-4 py-4')

        def render_tab(index: int):
            content_area.clear()
            with content_area.classes('animate-fade-in'):
                on_tab_change(index)

        render_tab(current_index["value"])

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

    # Animate underline position on first render
    ui.timer(0.2, lambda: move_indicator(current_index["value"]), once=True)