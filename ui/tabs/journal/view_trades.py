from nicegui import ui
from data.db import get_all_trades
from ui.components.trade_detail import render_trade_detail

def render():
    with ui.column().classes('w-full max-w-7xl mx-auto'):
        ui.label('📘 Trade History').classes('text-2xl font-bold mb-4 text-purple-300')

        trades = get_all_trades()

        columns = [
            {'name': 'datetime', 'label': 'Date', 'field': 'datetime'},
            {'name': 'market', 'label': 'Market', 'field': 'market'},
            {'name': 'session', 'label': 'Session', 'field': 'session'},
            {'name': 'ht_bias', 'label': 'Bias', 'field': 'ht_bias'},
            {'name': 'execution_context', 'label': 'Exec Ctx', 'field': 'execution_context'},
        ]

        ui.table(columns=columns, rows=trades, row_key='id')

        ui.separator().classes('my-4')

        for trade in trades:
            with ui.expansion(f"{trade['datetime']} – {trade['market']} – {trade['session']}").classes('my-2'):
                render_trade_detail(trade)