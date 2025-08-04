from nicegui import ui
from agents.coach_registry import get_registered_coaches
from utils.prompts import list_prompt_versions

def render_coach_feedback(trade: dict):
    with ui.column().classes('w-full gap-4 mt-6'):
        ui.label('🧠 Run AI Coach Feedback').classes('text-lg font-bold text-purple-300')

        coaches = get_registered_coaches()
        coach_names = list(coaches.keys())

        selected_coach = ui.select(coach_names, label='Select Coach').classes('w-64')
        selected_version = ui.select([], label='Select Version').classes('w-32')

        # Update version dropdown dynamically
        def update_versions():
            coach_name = selected_coach.value
            if coach_name:
                coach_class = coaches[coach_name]
                category = coach_class.category  # 🔁 FIXED LINE
                versions = list_prompt_versions(category)
                selected_version.options = versions
                if versions:
                    selected_version.value = versions[0]

        selected_coach.on('update:model-value', update_versions)

        output_area = ui.label('').classes('text-sm text-gray-300 whitespace-pre-wrap')

        def run_feedback():
            coach_name = selected_coach.value
            version = selected_version.value
            if not coach_name or not version:
                output_area.text = 'Please select both coach and version.'
                return

            CoachClass = coaches[coach_name]
            coach = CoachClass(version=version)
            feedback = coach.generate_feedback(trade)
            output_area.text = feedback

        ui.button('Run Feedback', on_click=run_feedback).classes('w-48 bg-blue-700 text-white hover:bg-blue-800')
        output_area