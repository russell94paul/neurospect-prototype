from nicegui import ui

inputs = {}

def render():
    ui.label('📊 Orderflow Confirmation').classes('text-lg text-purple-300 font-semibold')
    ui.separator().classes('my-2')

    with ui.element('div').classes('flex flex-row gap-6 !flex-nowrap !items-start w-full'):

        # Left column
        with ui.element('div').classes('w-1/2 flex flex-col gap-4'):
            inputs['confirmations'] = ui.select(
                ['Delta Reversal', 'Imbalance Stack', 'Absorption', 'Divergence', 'Footprint Reversal', 'Speed Spike'],
                label='Confirmation Used',
                multiple=True
            ).classes('w-full')

            inputs['cvd_behavior'] = ui.select(
                ['Bullish', 'Bearish', 'Divergent', 'Aligned'],
                label='CVD Behavior'
            ).classes('w-full')

            inputs['tape_behavior'] = ui.select(
                ['Aggression', 'Absorption', 'Spoofing', 'Passive Buyers/Sellers'],
                label='Tape Behavior'
            ).classes('w-full')

        # Right column
        with ui.element('div').classes('w-1/2 flex flex-col gap-4'):
            inputs['footprint_notes'] = ui.textarea('Footprint Snapshot Notes').classes('w-full')
            # ✅ boolean control → use switch, not toggle
            inputs['orderflow_match'] = ui.switch('Did Orderflow confirm ICT bias?').classes('mt-2')


def get_data():
    return {
        'confirmations': ','.join(inputs['confirmations'].value or []) if 'confirmations' in inputs else None,
        'cvd_behavior': inputs['cvd_behavior'].value if 'cvd_behavior' in inputs else None,
        'tape_behavior': inputs['tape_behavior'].value if 'tape_behavior' in inputs else None,
        'footprint_notes': inputs['footprint_notes'].value if 'footprint_notes' in inputs else None,
        # store as 0/1 integer for your INTEGER column
        'orderflow_match': 1 if inputs.get('orderflow_match') and inputs['orderflow_match'].value else 0,
    }