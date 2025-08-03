from nicegui import ui

inputs = {}

def render():
    ui.label('📈 Market Context').classes('text-lg text-purple-300 font-semibold')
    ui.separator().classes('my-2')

    with ui.element('div').classes('flex flex-row gap-6 !flex-nowrap !items-start w-full'):

        with ui.element('div').classes('w-1/2 flex flex-col gap-4'):
            inputs['bias'] = ui.select(
                ['Bullish', 'Bearish', 'Neutral'],
                label='Market Bias'
            ).classes('w-full')

            inputs['structure'] = ui.select(
                ['Trending Up', 'Trending Down', 'Rangebound', 'Breakout Setup'],
                label='Market Structure'
            ).classes('w-full')

        with ui.element('div').classes('w-1/2 flex flex-col gap-4'):
            inputs['key_levels'] = ui.input('Key HTF Levels Tagged (comma-separated)').classes('w-full')

            inputs['vol_profile'] = ui.select(
                ['Low Volume Node', 'High Volume Node', 'POC Tagged', 'Value Area Rotation'],
                label='Volume Profile Context',
                multiple=True
            ).classes('w-full')

def get_data():
    return {
        'bias': inputs['bias'].value,
        'structure': inputs['structure'].value,
        'key_levels': inputs['key_levels'].value,
        'vol_profile': ','.join(inputs['vol_profile'].value or []),
    }