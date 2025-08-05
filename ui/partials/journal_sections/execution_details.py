from nicegui import ui

inputs = {}

def render():
    ui.label('🎯 Execution Details').classes('text-lg text-purple-300 font-semibold')
    ui.separator().classes('my-2')

    with ui.element('div').classes('flex flex-row gap-6 !flex-nowrap !items-start w-full'):

        # Left column
        with ui.element('div').classes('w-1/2 flex flex-col gap-4'):
            inputs['direction'] = ui.select(['Long', 'Short'], label='Direction').classes('w-full')
            inputs['entry_method'] = ui.select(['Limit', 'Market', 'Stop'], label='Entry Method').classes('w-full')
            inputs['entry_type'] = ui.select(
                ['OB', 'FVG', 'Breaker', 'Sweep', 'POC Test', 'LVN Fade', 'Other'],
                label='Entry Type'
            ).classes('w-full')

            # Entry time as time-only (DB column is TEXT); keep it simple and consistent with your metadata date
            inputs['entry_time'] = ui.input('Entry Time (HH:MM)').props('type=time').classes('w-full')

        # Right column
        with ui.element('div').classes('w-1/2 flex flex-col gap-4'):
            inputs['entry_price']  = ui.input('Entry Price').props('type=number step=0.01').classes('w-full')
            inputs['stop_loss']    = ui.input('Stop Loss').props('type=number step=0.01').classes('w-full')
            inputs['take_profit']  = ui.input('Take Profit').props('type=number step=0.01').classes('w-full')
            inputs['rr_entry']     = ui.input('RR at Entry').props('type=number step=0.01').classes('w-full')

            inputs['execution_level'] = ui.select(
                ['LTF OB', '1m FVG', '3m FVG', '5m FVG', 'LVN', 'HVN', 'VP Gap', 'POC Test', 'Value Edge', 'Other'],
                label='Execution Level(s)',
                multiple=True
            ).classes('w-full')


def get_data():
    # Helper to safely convert number-like inputs to float or None
    def _to_float(key):
        val = inputs[key].value if key in inputs else None
        if val in (None, '', 'None'):
            return None
        try:
            return float(val)
        except Exception:
            return None

    return {
        # Section 3: Execution Details (match DB column names exactly)
        'direction': inputs['direction'].value if 'direction' in inputs else None,
        'entry_method': inputs['entry_method'].value if 'entry_method' in inputs else None,
        'entry_type': inputs['entry_type'].value if 'entry_type' in inputs else None,
        'entry_time': inputs['entry_time'].value if 'entry_time' in inputs else None,
        'entry_price': _to_float('entry_price'),
        'stop_loss': _to_float('stop_loss'),
        'take_profit': _to_float('take_profit'),
        'rr_entry': _to_float('rr_entry'),
        # Store multi-select as comma-separated string (consistent with your metadata design)
        'execution_level': ','.join(inputs['execution_level'].value or []) if 'execution_level' in inputs else None,
    }