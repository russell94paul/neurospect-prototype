from nicegui import ui
from datetime import date

inputs = {}

def render():
    ui.label('🗂️ Trade Metadata').classes('text-lg text-purple-300 font-semibold')
    ui.separator().classes('my-2')

    with ui.element('div').classes('flex flex-row gap-6 !flex-nowrap !items-start w-full'):

        with ui.element('div').classes('w-1/2 flex flex-col gap-4'):
            inputs['market'] = ui.select(['ES', 'NQ', 'CL', '6E'], label='Market').classes('w-full')
            inputs['session'] = ui.select(['Asia', 'London', 'NY AM', 'NY PM'], label='Session').classes('w-full')
            inputs['account_type'] = ui.select(['Sim', 'Live', 'Evaluation'], label='Account Type').classes('w-full')

        with ui.element('div').classes('w-1/2 flex flex-col gap-4'):
            inputs['datetime'] = ui.input('Date (YYYY-MM-DD)').props('type=date').classes('w-full')
            inputs['datetime'].value = str(date.today())

            inputs['execution_context'] = ui.select(
                ['News', 'Open', 'Killzone', 'Closing Session'],
                label='Execution Context',
                multiple=True
            ).classes('w-full')

def get_data():
    return {
        'market': inputs['market'].value,
        'session': inputs['session'].value,
        'datetime': inputs['datetime'].value,
        'account_type': inputs['account_type'].value,
        'execution_context': ','.join(inputs['execution_context'].value or []),
    }