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

    # Feedback card container with glowing hover and pulse
    with ui.card().classes(
        'bg-[#0f0f1c] text-white p-6 rounded-2xl shadow-lg max-w-5xl w-full '
        'transition-all duration-300 border border-purple-500 '
        'hover:shadow-[0_0_25px_7px_rgba(168,85,247,0.8)] animate-pulse'
    ):
        output_area = ui.markdown('⏳ *Waiting for analysis...*').classes('text-sm font-mono')

    def update_feedback(version):
        output_area.content = '⏳ *Analyzing entire trade history...*'
        try:
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

    dropdown.on('update:model-value', lambda _: None)

    ui.button('🚀 Run Feedback', on_click=lambda: update_feedback(dropdown.value)) \
        .classes('mt-2 bg-gradient-to-r from-purple-500 to-blue-500 text-white font-semibold px-4 py-2 rounded shadow-md hover:shadow-lg transition-all duration-300')