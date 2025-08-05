from nicegui import ui

inputs = {}

def render():
    ui.label('📝 Reflection & Tagging').classes('text-lg text-purple-300 font-semibold')
    ui.separator().classes('my-2')

    with ui.element('div').classes('flex flex-row gap-6 !flex-nowrap !items-start w-full'):

        # Left column
        with ui.element('div').classes('w-1/2 flex flex-col gap-4'):
            inputs['followed_plan'] = ui.switch('Did you follow your plan?').classes('mt-1')

            inputs['grade'] = ui.select(
                ['A+', 'A', 'B', 'C', 'F'],
                label='Trade Quality Grade'
            ).classes('w-full')

            inputs['what_went_well'] = ui.textarea('What went well').classes('w-full')

        # Right column
        with ui.element('div').classes('w-1/2 flex flex-col gap-4'):
            inputs['what_needs_improvement'] = ui.textarea('What needs improvement').classes('w-full')

            inputs['tags'] = ui.select(
                ['VP Confluence', 'ICT Model', 'Misread OF', 'Overtraded', 'Perfect Execution',
                 'Risk Discipline', 'Late Entry', 'Chopped', 'News Impact'],
                label='Tags',
                multiple=True
            ).classes('w-full')

            inputs['setup_label'] = ui.input('Label the setup').classes('w-full')


def get_data():
    return {
        # Section 8: Reflection
        'followed_plan': 1 if inputs.get('followed_plan') and inputs['followed_plan'].value else 0,
        'grade': inputs['grade'].value if 'grade' in inputs else None,
        'what_went_well': inputs['what_went_well'].value if 'what_went_well' in inputs else None,
        'what_needs_improvement': inputs['what_needs_improvement'].value if 'what_needs_improvement' in inputs else None,
        'tags': ','.join(inputs['tags'].value or []) if 'tags' in inputs else None,
        'setup_label': inputs['setup_label'].value if 'setup_label' in inputs else None,
    }