import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).parent / 'journal.db'

def init_db():
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS journal_entries (
                id INTEGER PRIMARY KEY AUTOINCREMENT,

                -- Section 1: Trade Metadata
                market TEXT,
                session TEXT,
                datetime TEXT,
                account_type TEXT,
                execution_context TEXT,

                -- Section 2: Market Context
                ht_bias TEXT,
                daily_narrative TEXT,
                killzone TEXT,
                smt_present INTEGER,
                pd_arrays TEXT,
                liquidity_targeted TEXT,
                mp_context TEXT,
                vp_context TEXT,

                -- Section 3: Execution Details
                direction TEXT,
                entry_method TEXT,
                entry_type TEXT,
                entry_time TEXT,
                entry_price REAL,
                stop_loss REAL,
                take_profit REAL,
                rr_entry REAL,
                execution_level TEXT,

                -- Section 4: Orderflow Confirmation
                confirmations TEXT,
                cvd_behavior TEXT,
                tape_behavior TEXT,
                footprint_notes TEXT,
                orderflow_match INTEGER,

                -- Section 5: Trade Management
                management_style TEXT,
                stop_moved INTEGER,
                violated_plan INTEGER,
                exit_method TEXT,
                adjustment_notes TEXT,

                -- Section 6: Outcome & Metrics
                result TEXT,
                exit_price REAL,
                exit_time TEXT,
                pnl REAL,
                r_multiple REAL,
                mfe REAL,
                mae REAL,
                mp_outcome TEXT,
                of_match INTEGER,

                -- Section 7: Emotional State
                state_before TEXT,
                confidence_level INTEGER,
                state_after TEXT,
                mindset_tags TEXT,
                mental_notes TEXT,

                -- Section 8: Reflection
                followed_plan INTEGER,
                grade TEXT,
                what_went_well TEXT,
                what_needs_improvement TEXT,
                tags TEXT,
                setup_label TEXT,

                -- AI Agent Feedback
                narrative_feedback TEXT,
                execution_feedback TEXT
            )
        ''')
        conn.commit()

def save_journal_entry(data: dict):
    with sqlite3.connect(DB_PATH) as conn:
        keys = ', '.join(data.keys())
        placeholders = ', '.join('?' for _ in data)
        values = tuple(data.values())
        conn.execute(f'INSERT INTO journal_entries ({keys}) VALUES ({placeholders})', values)
        conn.commit()