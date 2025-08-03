from nicegui import ui

def render():
    with ui.column().classes('gap-4'):

        ui.label('🧭 Market Context & Setup').classes('text-lg text-purple-300 font-semibold')

        with ui.row().classes('w-full gap-4'):
            ui.date(label='Date').classes('w-1/2')
            ui.select(['Asia', 'London', 'NY AM', 'NY PM'], label='Session').classes('w-1/2')

        with ui.row().classes('w-full gap-4'):
            ui.select(['ES', 'NQ', 'CL', '6E'], label='Market Symbol').classes('w-1/2')
            ui.select(['Sim', 'Live', 'Evaluation'], label='Account Type').classes('w-1/2')

        with ui.row().classes('w-full gap-4'):
            ui.select(['Bullish', 'Bearish', 'Neutral'], label='Market Bias').classes('w-1/2')
            ui.select(['OB', 'FVG', 'Breaker', 'Liquidity Void', 'TDOB', 'None'],
                      label='Key PD Array').classes('w-1/2')

        ui.textarea(label='Daily Narrative').props('autogrow').classes('w-full')

        with ui.row().classes('w-full gap-4'):
            ui.toggle(text='SMT Present?', value=False).classes('w-1/3')
            ui.select(['Buy-side', 'Sell-side', 'Internal', 'External'], label='Liquidity Targeted').classes('w-2/3')

        ui.label('📊 Volume / Market Profile Context').classes('text-md text-blue-300 font-semibold')

        with ui.column().classes('gap-2'):
            ui.checkbox('Inside Value Area')
            ui.checkbox('POC Shift')
            ui.checkbox('LVN Rejection')
            ui.checkbox('Value Area Rejection')
            ui.checkbox('Volume Spike or Anomaly')
