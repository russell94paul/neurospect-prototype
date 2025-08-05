from nicegui import ui
from data.db import get_all_trades
from agents.pattern_detection_coach import PatternDetectionCoach
from utils.prompts import list_prompt_versions, load_prompt


def render():
    ui.label('🧠 Pattern Detection Feedback').classes('text-2xl font-bold text-purple-300 mb-4')

    versions = list_prompt_versions(PatternDetectionCoach.category)
    selected_version = versions[0] if versions else 'v1'

    dropdown = ui.select(
        options=versions,
        value=selected_version,
        label='Prompt Version',
    ).classes('w-48 mb-4')

    # Feedback card container
    with ui.card().classes('bg-[#1a1a2e] text-white p-6 rounded-xl shadow-lg max-w-5xl w-full'):
        output_area = ui.markdown('⏳ *Waiting for analysis...*').classes('text-sm font-mono')

    def update_feedback(version):
        output_area.content = '⏳ *Analyzing entire trade history...*'
        try:
            # Load prompt properly and assign it
            coach = PatternDetectionCoach(version)

            trades = get_all_trades()
            if not trades:
                output_area.content = '⚠️ No trades found.'
                return

            formatted_input = coach.format_input(trades)
            feedback = coach.run(formatted_input)

            output_area.content = f'### ✅ Pattern Detection Result\n\n{feedback}'

        except Exception as e:
            output_area.content = f'❌ Error during feedback generation:\n```\n{str(e)}\n```'

    # Wire dropdown version change
    dropdown.on('update:model-value', lambda _: None)  # no auto-refresh on change

    # Run button
    ui.button('🚀 Run Feedback', on_click=lambda: update_feedback(dropdown.value)) \
        .classes('mt-2 bg-gradient-to-r from-purple-500 to-blue-500 text-white font-semibold px-4 py-2 rounded shadow-md hover:shadow-lg transition-all duration-300')