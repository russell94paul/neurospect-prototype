from nicegui import ui
from ui.components.coach_feedback import render_coach_feedback

def render_trade_detail(trade: dict):
    with ui.column().classes('gap-4'):

        # --- Metadata ---
        ui.label('📁 Metadata').classes('text-lg font-bold text-blue-300')
        with ui.element('div').classes('grid grid-cols-1 md:grid-cols-2 gap-4 w-full'):
            ui.label(f"Market: {trade.get('market', '-')}")
            ui.label(f"Session: {trade.get('session', '-')}")
            ui.label(f"Account Type: {trade.get('account_type', '-')}")
            ui.label(f"Execution Context: {trade.get('execution_context', '-')}")

        ui.separator()

        # --- Market Context ---
        ui.label('📊 Market Context').classes('text-lg font-bold text-blue-300')
        with ui.element('div').classes('grid grid-cols-1 md:grid-cols-2 gap-4 w-full'):
            ui.label(f"Bias: {trade.get('ht_bias', '-')}")
            ui.label(f"Market Structure: {trade.get('market_structure', '-')}")
            ui.label(f"HTF Levels Tagged: {trade.get('key_levels', '-')}")
            ui.label(f"Killzone: {trade.get('killzone', '-')}")
            ui.label(f"SMT Present: {'✅' if trade.get('smt_present') else '—'}")
            ui.label(f"PD Arrays: {trade.get('pd_arrays', '-')}")
            ui.label(f"Liquidity Targeted: {trade.get('liquidity_targeted', '-')}")
            ui.label(f"MP Context: {trade.get('mp_context', '-')}")
            ui.label(f"Volume Profile Context: {trade.get('vol_profile', '-')}")

        ui.separator()

        # --- Execution Details ---
        ui.label('🎯 Execution Details').classes('text-lg font-bold text-red-400')
        with ui.element('div').classes('grid grid-cols-1 md:grid-cols-2 gap-4 w-full'):
            ui.label(f"Direction: {trade.get('direction', '-')}")
            ui.label(f"Entry Type: {trade.get('entry_type', '-')}")
            ui.label(f"Entry Price: {trade.get('entry_price', '-')}")
            ui.label(f"Take Profit: {trade.get('take_profit', '-')}")
            ui.label(f"RR at Entry: {trade.get('rr_entry', '-')}")
            ui.label(f"Entry Method: {trade.get('entry_method', '-')}")
            ui.label(f"Entry Time: {trade.get('entry_time', '-')}")
            ui.label(f"Stop Loss: {trade.get('stop_loss', '-')}")
            ui.label(f"Execution Level: {trade.get('execution_level', '-')}")

        ui.separator()

        # --- Outcome & Metrics ---
        ui.label('📈 Outcome & Metrics').classes('text-lg font-bold text-green-400')
        with ui.element('div').classes('grid grid-cols-1 md:grid-cols-2 gap-4 w-full'):
            ui.label(f"Result: {trade.get('result', '-')}")
            ui.label(f"Exit Price: {trade.get('exit_price', '-')}")
            ui.label(f"PnL: {trade.get('pnl', '-')}")
            ui.label(f"MFE: {trade.get('mfe', '-')}")
            ui.label(f"Exit Time: {trade.get('exit_time', '-')}")
            ui.label(f"R Multiple: {trade.get('r_multiple', '-')}")
            ui.label(f"MAE: {trade.get('mae', '-')}")
            ui.label(f"MP Outcome: {trade.get('mp_outcome', '-')}")

        ui.separator()

        # --- Reflection ---
        ui.label('🪞 Reflection').classes('text-lg font-bold text-purple-400')
        with ui.element('div').classes('grid grid-cols-1 md:grid-cols-2 gap-4 w-full'):
            ui.label(f"Followed Plan: {'✅' if trade.get('followed_plan') else '❌'}")
            ui.label(f"Grade: {trade.get('grade', '-')}")
            ui.label(f"What Went Well: {trade.get('what_went_well', '-')}")
            ui.label(f"What Needs Improvement: {trade.get('what_needs_improvement', '-')}")
            ui.label(f"Tags: {trade.get('tags', '-')}")
            ui.label(f"Setup Label: {trade.get('setup_label', '-')}")

        ui.separator()

        # --- Attachments ---
        ui.label('📎 Attachments').classes('text-lg font-bold text-yellow-300')
        with ui.element('div').classes('grid grid-cols-1 md:grid-cols-2 gap-4 w-full'):
            ui.label(f"Entry Screenshot: {trade.get('entry_screenshot', '-')}")
            ui.label(f"Footprint Snapshot: {trade.get('footprint_snapshot', '-')}")
            ui.label(f"Volume/MP Chart: {trade.get('volume_mp_chart', '-')}")
            ui.label(f"Audio Commentary: {trade.get('audio_commentary', '-')}")
            ui.label(f"OF/DOM Log: {trade.get('of_dom_log', '-')}")

        ui.separator()

        # --- AI Coach Feedback Panel ---
        render_coach_feedback(trade)