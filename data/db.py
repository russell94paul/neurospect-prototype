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
                market_structure TEXT,
                key_levels TEXT,
                killzone TEXT,
                smt_present INTEGER,
                pd_arrays TEXT,
                liquidity_targeted TEXT,
                mp_context TEXT,
                vol_profile TEXT,

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

                -- AI Feedback (Core Coaches)
                psychology_feedback TEXT,
                psychology_feedback_version TEXT,

                risk_feedback TEXT,
                risk_feedback_version TEXT,

                narrative_feedback TEXT,
                narrative_feedback_version TEXT,

                execution_feedback TEXT,
                execution_feedback_version TEXT,

                drill_feedback TEXT,
                drill_feedback_version TEXT,

                summary_feedback TEXT,
                summary_feedback_version TEXT,

                -- Experimental Coaches
                pattern_feedback TEXT,
                pattern_feedback_version TEXT,

                setup_audit_feedback TEXT,
                setup_audit_feedback_version TEXT,

                conviction_feedback TEXT,
                conviction_feedback_version TEXT
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


def get_all_trades():
    with sqlite3.connect(DB_PATH) as conn:
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM journal_entries ORDER BY datetime DESC')
        rows = cursor.fetchall()
        return [dict(row) for row in rows]


def update_feedback(entry_id: int, field: str, content: str, version: str = None):
    version_field = f"{field}_version" if version else None
    with sqlite3.connect(DB_PATH) as conn:
        if version_field:
            conn.execute(f'''
                UPDATE journal_entries 
                SET {field} = ?, {version_field} = ? 
                WHERE id = ?
            ''', (content, version, entry_id))
        else:
            conn.execute(f'''
                UPDATE journal_entries 
                SET {field} = ? 
                WHERE id = ?
            ''', (content, entry_id))
        conn.commit()


def reset_db():
    DB_PATH.unlink(missing_ok=True)
    init_db()