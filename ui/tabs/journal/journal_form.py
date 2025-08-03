from ui.partials.journal_sections import context_and_setup
from nicegui import ui

def render():
    with ui.card().classes('w-full max-w-4xl bg-[#1a1a2e] text-white shadow-md'):
        with ui.column().classes('p-6 gap-6'):
            ui.label('🧠 Structured Journal Form').classes('text-xl font-bold text-purple-400')
            ui.label('Track setups, behavior, outcome, and psychology with precision.').classes('text-sm text-gray-400')

            context_and_setup.render()