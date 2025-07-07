from pathlib import Path
import pandas as pd
import sqlite3
import os
from datetime import datetime

# Define centralized paths
DATA_DIR = Path(__file__).parent.parent / "data"
CSV_PATH = DATA_DIR / "trade_log.csv"
DB_PATH = DATA_DIR / "trades.db"

# Ensure the data folder exists
DATA_DIR.mkdir(parents=True, exist_ok=True)

import hashlib

def save_trade(trade_data: dict, mode="csv"):
    # Convert screenshot list to semicolon-separated string
    if "screenshots" in trade_data and isinstance(trade_data["screenshots"], list):
        trade_data["screenshots"] = ";".join(trade_data["screenshots"])

    # === Compute hash to avoid duplicates ===
    key = f"{trade_data.get('trade_date')}_{trade_data.get('entry_time')}_{trade_data.get('instrument')}"
    trade_hash = hashlib.md5(key.encode()).hexdigest()
    trade_data["trade_hash"] = trade_hash

    df_new = pd.DataFrame([trade_data])
    df_new["timestamp"] = datetime.now().isoformat()

    if mode == "csv":
        if CSV_PATH.exists():
            try:
                df_existing = pd.read_csv(CSV_PATH)

                for col in df_existing.columns:
                    if col not in df_new.columns:
                        df_new[col] = None
                for col in df_new.columns:
                    if col not in df_existing.columns:
                        df_existing[col] = None

                df_new = df_new[df_existing.columns]
                df_new.to_csv(CSV_PATH, mode='a', header=False, index=False)
            except Exception as e:
                raise RuntimeError(f"Failed to align and append to CSV: {e}")
        else:
            df_new.to_csv(CSV_PATH, index=False)

    elif mode == "sqlite":
        try:
            conn = sqlite3.connect(DB_PATH)
            cursor = conn.cursor()

            # Ensure table exists with hash constraint
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS trades (
                    trade_date DATE,
                    entry_time TIME,
                    exit_time TIME,
                    instrument TEXT,
                    direction TEXT,
                    entry_type TEXT,
                    risk_level INTEGER,
                    partial_exit INTEGER,
                    profit_points REAL,
                    execution_quality TEXT,
                    session TEXT,
                    news_today TEXT,
                    account_type TEXT,
                    drawdown_proximity TEXT,
                    eval_progress TEXT,
                    days_left INTEGER,
                    payout_proximity TEXT,
                    sleep_quality TEXT,
                    caffeine TEXT,
                    distractions TEXT,
                    emotional_regulation INTEGER,
                    routine_done INTEGER,
                    reviewed_plan INTEGER,
                    bias_prepped INTEGER,
                    risk_today TEXT,
                    matches_plan TEXT,
                    setup_grade TEXT,
                    prep_time TEXT,
                    notes TEXT,
                    emotionally_driven INTEGER,
                    reflection TEXT,
                    screenshot_taken INTEGER,
                    screenshots TEXT,
                    llm_feedback_json TEXT,
                    llm_feedback_summary TEXT,
                    timestamp TEXT,
                    trade_hash TEXT NOT NULL UNIQUE
                )
            """)

            try:
                df_new.to_sql("trades", conn, if_exists="append", index=False)
            except sqlite3.IntegrityError:
                print("⚠️ Duplicate trade detected. Skipping insert.")
            finally:
                conn.close()

        except Exception as e:
            raise RuntimeError(f"Failed to save to SQLite: {e}")

    else:
        raise ValueError(f"Unsupported storage mode: {mode}")


def load_trades(mode="csv"):
    if mode == "csv":
        if not CSV_PATH.exists():
            return pd.DataFrame()
        try:
            df = pd.read_csv(CSV_PATH)
            return df
        except Exception as e:
            raise RuntimeError(f"Failed to load CSV: {e}")

    elif mode == "sqlite":
        if not DB_PATH.exists():
            return pd.DataFrame()
        try:
            return pd.read_sql("SELECT * FROM trades", sqlite3.connect(DB_PATH))
        except Exception as e:
            raise RuntimeError(f"Failed to load SQLite DB: {e}")

    else:
        raise ValueError(f"Unsupported storage mode: {mode}")
    
    
# === DEBUGGING SCHEMA ===
def check_schema():
    import sqlite3
    from config import SQLITE_DB_PATH

    conn = sqlite3.connect(SQLITE_DB_PATH)
    cursor = conn.cursor()
    cursor.execute("PRAGMA table_info(trades)")
    print("\n📋 Trade Table Schema:")
    for row in cursor.fetchall():
        print(row)
    conn.close()
    
if __name__ == "__main__":
    check_schema()