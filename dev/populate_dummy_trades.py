import random
from datetime import datetime, timedelta
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from data.db import save_journal_entry

markets = ['ES', 'NQ', 'CL', '6E']
sessions = ['Asia', 'London', 'NY AM', 'NY PM']
account_types = ['Sim', 'Live', 'Evaluation']
biases = ['Bullish', 'Bearish', 'Consolidating']
directions = ['Long', 'Short']
grades = ['A+', 'A', 'B', 'C', 'F']
results = ['Full TP', 'Partial', 'BE', 'SL', 'Manual Exit']
mindset_tags_list = ['FOMO', 'Hesitant', 'Flow', 'Tilt', 'Greedy', 'Perfect Execution']

def random_trade(offset_days=0):
    dt = datetime.now() - timedelta(days=offset_days)
    entry_price = round(random.uniform(4300, 4400), 2)
    stop_loss = round(entry_price - random.uniform(3, 10), 2)
    take_profit = round(entry_price + random.uniform(5, 15), 2)

    return {
        # Section 1: Trade Metadata
        "market": random.choice(markets),
        "session": random.choice(sessions),
        "datetime": dt.strftime("%Y-%m-%d"),
        "account_type": random.choice(account_types),
        "execution_context": "Killzone,News",

        # Section 2: Market Context
        "ht_bias": random.choice(biases),
        "market_structure": "Higher Highs / Higher Lows",
        "key_levels": "Yesterday's High, Weekly Open",
        "killzone": "NY AM",
        "smt_present": random.randint(0, 1),
        "pd_arrays": "FVG,OB",
        "liquidity_targeted": "Buy-side",
        "mp_context": "POC Shift",
        "vol_profile": "LVN Rejection",

        # Section 3: Execution Details
        "direction": random.choice(directions),
        "entry_method": "Limit",
        "entry_type": "OB",
        "entry_time": dt.strftime("%H:%M"),
        "entry_price": entry_price,
        "stop_loss": stop_loss,
        "take_profit": take_profit,
        "rr_entry": round((take_profit - entry_price) / (entry_price - stop_loss), 2),
        "execution_level": "1-min FVG",

        # Section 4: Orderflow Confirmation
        "confirmations": "Delta Reversal,Imbalance Stack",
        "cvd_behavior": "Aligned",
        "tape_behavior": "Aggression",
        "footprint_notes": "Saw strong imbalance flipping into key OB",
        "orderflow_match": 1,

        # Section 5: Trade Management
        "management_style": "Let it run",
        "stop_moved": 1,
        "violated_plan": 0,
        "exit_method": "Manual",
        "adjustment_notes": "Took profit near LVN edge",

        # Section 6: Outcome & Metrics
        "result": random.choice(results),
        "exit_price": take_profit,
        "exit_time": dt.strftime("%H:%M"),
        "pnl": round(random.uniform(50, 250), 2),
        "r_multiple": round(random.uniform(0.5, 2.5), 2),
        "mfe": round(random.uniform(5, 10), 2),
        "mae": round(random.uniform(2, 6), 2),
        "mp_outcome": "Rotated Through LVN",
        "of_match": 1,

        # Section 7: Emotional & Cognitive State
        "state_before": "Focused",
        "confidence_level": random.randint(5, 10),
        "state_after": random.choice(["Calm", "Frustrated", "Satisfied"]),
        "mindset_tags": ",".join(random.sample(mindset_tags_list, 2)),
        "mental_notes": "Entered well but hesitated on adding size",

        # Section 8: Reflection & Tagging
        "followed_plan": 1,
        "grade": random.choice(grades),
        "what_went_well": "Execution on level with confirmation was clean",
        "what_needs_improvement": "Still hesitating on second entries",
        "tags": "ICT Model,VP Confluence",
        "setup_label": "NY OB + LVN Fade",

        # Section 9: Attachments
        "entry_screenshot": "",
        "footprint_snapshot": "",
        "volume_mp_chart": "",
        "audio_commentary": "",
        "of_dom_log": "",

        # Coach feedback placeholders
        "psychology_feedback": "",
        "psychology_feedback_version": "",
        "risk_feedback": "",
        "risk_feedback_version": "",
        "narrative_feedback": "",
        "narrative_feedback_version": "",
        "execution_feedback": "",
        "execution_feedback_version": "",
        "drill_feedback": "",
        "drill_feedback_version": "",
        "summary_feedback": "",
        "summary_feedback_version": "",
        "pattern_feedback": "",
        "pattern_feedback_version": "",
        "setup_audit_feedback": "",
        "setup_audit_feedback_version": "",
        "conviction_feedback": "",
        "conviction_feedback_version": "",
    }

# Generate 15 entries
num_trades = 30
for i in range(num_trades):
    entry = random_trade(offset_days=i)
    save_journal_entry(entry)

print(f"✅ {num_trades} dummy trades inserted into journal.db")