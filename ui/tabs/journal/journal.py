from nicegui import ui
from components.sticky_section import sticky_section

from tabs.journal import (
    journal_form,
    screenshots,
    trade_feedback,
    tradeflex_generator,
    export_to_mirror_toggle,
    audio_debrief,
    view_trades
)

selected_tab = {'value': 'form'}

def render():

    @ui.refreshable
    def tab_bar():
        with ui.column().classes('w-full'):
            ui.label("📓 Journal Your Trade").classes("text-xl font-bold text-purple-400 pl-2 pb-1")

            with ui.row().classes(
                'justify-center gap-2 items-center px-2 py-2'
            ):
                def tab_btn(label: str, key: str, icon: str):
                    def on_click():
                        selected_tab['value'] = key
                        tab_bar.refresh()
                        section.refresh()

                    is_active = selected_tab['value'] == key
                    ui.button(icon=icon, text=label, on_click=on_click).classes(
                        'h-14 px-6 text-nowrap text-white font-semibold rounded-xl shadow-md transition-all '
                        'hover:scale-[1.02] '
                        + (
                            'bg-gradient-to-br from-purple-500 to-blue-500'
                            if is_active else
                            'bg-gradient-to-br from-[#1f1f38] to-[#161627]'
                        )
                    ).props('flat')

                tab_btn('Journal Form', 'form', 'note_alt')
                tab_btn('Screenshots', 'shots', 'photo')
                tab_btn('AI Feedback', 'feedback', 'insights')
                tab_btn('TradeFlex Generator', 'generator', 'memory')
                tab_btn('Export to Mirror', 'mirror', 'sync')
                tab_btn('Audio Debrief', 'audio', 'mic')
                tab_btn('View Past Trades', 'view', 'folder')

    @ui.refreshable
    def section():
        match selected_tab['value']:
            case 'form':
                journal_form.render()
            case 'shots':
                screenshots.render()
            case 'feedback':
                trade_feedback.render()
            case 'generator':
                tradeflex_generator.render()
            case 'mirror':
                export_to_mirror_toggle.render()
            case 'audio':
                audio_debrief.render()
            case 'view':
                view_trades.render()

    # The layout handles scroll and stickiness — no extra containers
    with sticky_section(tab_bar):
        section()