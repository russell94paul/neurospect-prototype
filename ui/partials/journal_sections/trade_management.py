from nicegui import ui

inputs = {}

def render():
    ui.label('📈 Trade Management').classes('text-lg text-purple-300 font-semibold')
    ui.separator().classes('my-2')

    with ui.element('div').classes('flex flex-row gap-6 !flex-nowrap !items-start w-full'):

        # Left column
        with ui.element('div').classes('w-1/2 flex flex-col gap-4'):
            inputs['management_style'] = ui.select(
                ['Let it run', 'Active', 'Scale', 'Partial'],
                label='Management Style'
            ).classes('w-full')

            inputs['stop_moved'] = ui.switch('Stop Moved During Trade?').classes('mt-2')
            inputs['violated_plan'] = ui.switch('Trade Violated Plan?').classes('mt-2')

        # Right column
        with ui.element('div').classes('w-1/2 flex flex-col gap-4'):
            inputs['exit_method'] = ui.select(
                ['Time-Based', 'Price-Based', 'Profile-Based', 'Manual'],
                label='Trail or Exit Method'
            ).classes('w-full')

            inputs['adjustment_notes'] = ui.textarea('Notes on Adjustments').classes('w-full')


def get_data():
    return {
        # Section 5: Trade Management (match DB columns exactly)
        'management_style': inputs['management_style'].value if 'management_style' in inputs else None,
        'stop_moved': 1 if inputs.get('stop_moved') and inputs['stop_moved'].value else 0,
        'violated_plan': 1 if inputs.get('violated_plan') and inputs['violated_plan'].value else 0,
        'exit_method': inputs['exit_method'].value if 'exit_method' in inputs else None,
        'adjustment_notes': inputs['adjustment_notes'].value if 'adjustment_notes' in inputs else None,
    }