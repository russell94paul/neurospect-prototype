from nicegui import ui
from ui.components.coach_feedback import render_coach_feedback

def render_trade_detail(trade: dict):
    with ui.column().classes('gap-2'):
        ui.label('📁 Metadata').classes('text-lg font-bold text-blue-300')
        ui.label(f"Market: {trade.get('market', '-')}")
        ui.label(f"Session: {trade.get('session', '-')}")
        ui.label(f"Account Type: {trade.get('account_type', '-')}")
        ui.label(f"Execution Context: {trade.get('execution_context', '-')}")

        ui.separator()

        ui.label('📊 Market Context').classes('text-lg font-bold text-blue-300')
        ui.label(f"Bias: {trade.get('ht_bias', '-')}")
        ui.label(f"Market Structure: {trade.get('market_structure', '-')}")
        ui.label(f"HTF Levels Tagged: {trade.get('key_levels', '-')}")
        ui.label(f"Volume Profile Context: {trade.get('vol_profile', '-')}")

        ui.separator()

        # 🧠 AI Feedback Panel
        render_coach_feedback(trade)