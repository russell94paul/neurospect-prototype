from nicegui import ui
from data.db import init_db, save_journal_entry
from ui.partials.journal_sections import trade_metadata, market_context

def render():
    init_db()

    with ui.row().classes('w-full justify-center'):
        with ui.card().classes('w-full max-w-6xl bg-[#1a1a2e] text-white shadow-md'):
            with ui.column().classes('p-6 gap-6 w-full'):

                ui.label('🧠 Structured Journal Form').classes('text-xl font-bold text-purple-400')
                ui.label('Track setups, behavior, outcome, and psychology with precision.').classes('text-sm text-gray-400')

                # ✅ This now uses full width as intended
                trade_metadata.render()

                
                market_context.render()

                def handle_submit():
                    data = {}
                    data.update(trade_metadata.get_data())
                    data.update(market_context.get_data())
                    save_journal_entry(data)
                    ui.notify('Trade journal entry saved.', type='positive')

                ui.button('Add Trade', on_click=handle_submit).classes(
                    'w-full bg-gradient-to-r from-purple-500 to-blue-500 text-white rounded-lg px-4 py-2 mt-4'
                )