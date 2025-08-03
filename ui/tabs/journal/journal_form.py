from nicegui import ui
from data.db import init_db, save_journal_entry
from ui.partials.journal_sections import trade_metadata, market_context

def render():
    init_db()

    with ui.row().classes('w-full justify-center'):
        with ui.element('div').classes(
            'transition-all duration-300 hover:shadow-[0_0_20px_4px_rgba(168,85,247,0.5)] '
            'shadow-[0_0_12px_2px_rgba(168,85,247,0.3)] ring-1 ring-purple-500/30 rounded-xl'
        ):
            with ui.card().classes('w-full max-w-6xl bg-[#1a1a2e] text-white rounded-xl'):
                with ui.column().classes('p-6 gap-6 w-full'):

                    ui.label('🧠 Structured Journal Form').classes('text-xl font-bold text-purple-400')
                    ui.label('Track setups, behavior, outcome, and psychology with precision.').classes('text-sm text-gray-400')

                    trade_metadata.render()
                    market_context.render()

                    def handle_submit():
                        data = {}
                        data.update(trade_metadata.get_data())
                        data.update(market_context.get_data())
                        save_journal_entry(data)
                        ui.notify('Trade journal entry saved.', type='positive')
                        

                    with ui.element('button') \
                        .on('click', handle_submit) \
                        .classes(
                            'w-full bg-gradient-to-r from-[#d946ef] to-[#6366f1] text-white '
                            'rounded-lg px-4 py-2 mt-4 font-bold tracking-wide '
                            'shadow-[0_0_12px_rgba(217,70,239,0.8)] '
                            'hover:shadow-[0_0_24px_rgba(217,70,239,1)] '
                            'transition-all duration-300 uppercase'
                        ):
                        ui.label('Add Trade').classes('text-white text-center')