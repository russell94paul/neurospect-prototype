from nicegui import ui

inputs = {}

def render():
    ui.label('📊 Outcome & Metrics').classes('text-lg text-purple-300 font-semibold')
    ui.separator().classes('my-2')

    with ui.element('div').classes('flex flex-row gap-6 !flex-nowrap !items-start w-full'):

        # Left column
        with ui.element('div').classes('w-1/2 flex flex-col gap-4'):
            inputs['result'] = ui.select(
                ['Full TP', 'Partial', 'BE', 'SL', 'Manual Exit'],
                label='Result'
            ).classes('w-full')

            inputs['exit_price'] = ui.input('Exit Price').props('type=number step=0.01').classes('w-full')
            inputs['exit_time'] = ui.input('Exit Time (HH:MM)').props('type=time').classes('w-full')
            inputs['pnl'] = ui.input('PnL').props('type=number step=0.01').classes('w-full')

        # Right column
        with ui.element('div').classes('w-1/2 flex flex-col gap-4'):
            inputs['r_multiple'] = ui.input('R-Multiple').props('type=number step=0.01').classes('w-full')
            inputs['mfe'] = ui.input('MFE (Max Favorable Excursion)').props('type=number step=0.01').classes('w-full')
            inputs['mae'] = ui.input('MAE (Max Adverse Excursion)').props('type=number step=0.01').classes('w-full')

            inputs['mp_outcome'] = ui.select(
                ['Rejected VA', 'Accepted into Value', 'Rotated Through LVN'],
                label='Market Profile Outcome'
            ).classes('w-full')

            inputs['of_match'] = ui.switch('Orderflow Outcome Match?').classes('mt-2')


def get_data():
    def _to_float(key):
        val = inputs[key].value if key in inputs else None
        if val in (None, '', 'None'):
            return None
        try:
            return float(val)
        except Exception:
            return None

    return {
        # Section 6: Outcome & Metrics
        'result': inputs['result'].value if 'result' in inputs else None,
        'exit_price': _to_float('exit_price'),
        'exit_time': inputs['exit_time'].value if 'exit_time' in inputs else None,
        'pnl': _to_float('pnl'),
        'r_multiple': _to_float('r_multiple'),
        'mfe': _to_float('mfe'),
        'mae': _to_float('mae'),
        'mp_outcome': inputs['mp_outcome'].value if 'mp_outcome' in inputs else None,
        'of_match': 1 if inputs.get('of_match') and inputs['of_match'].value else 0,
    }