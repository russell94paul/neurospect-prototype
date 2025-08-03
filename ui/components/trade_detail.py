from nicegui import ui
from agents.psychology_coach import PsychologyCoach
from data.db import update_feedback

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

        # 🧠 Psychology Coach Feedback Section
        ui.label('🧠 Psychology Coach Feedback').classes('text-lg font-bold text-green-400')
        ui.label(trade.get('psychology_feedback', 'No feedback yet.')) \
            .classes('text-sm text-gray-300 italic')

        def run_psychology_feedback():
            coach = PsychologyCoach(version='v1')
            feedback = coach.generate_feedback(trade)
            update_feedback(trade['id'], 'psychology_feedback', feedback, version='v1')
            ui.notify('🧠 Psychology feedback saved.')

        ui.button('Run Psychology Coach', on_click=run_psychology_feedback).props('color=purple')