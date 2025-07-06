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

def save_trade(trade_data: dict, mode="csv"):
    # Convert screenshot list to semicolon-separated string if needed
    if "screenshots" in trade_data and isinstance(trade_data["screenshots"], list):
        trade_data["screenshots"] = ";".join(trade_data["screenshots"])

    df_new = pd.DataFrame([trade_data])

    if mode == "csv":
        if CSV_PATH.exists():
            try:
                df_existing = pd.read_csv(CSV_PATH)

                # Add any missing columns in new data
                for col in df_existing.columns:
                    if col not in df_new.columns:
                        df_new[col] = None

                # Add new columns to existing data if needed
                for col in df_new.columns:
                    if col not in df_existing.columns:
                        df_existing[col] = None

                # Align column order with existing CSV
                df_new = df_new[df_existing.columns]

                df_new.to_csv(CSV_PATH, mode='a', header=False, index=False)
            except Exception as e:
                raise RuntimeError(f"Failed to align and append to CSV: {e}")
        else:
            df_new.to_csv(CSV_PATH, index=False)

    elif mode == "sqlite":
        try:
            conn = sqlite3.connect(DB_PATH)
            df_new["timestamp"] = datetime.now().isoformat()
            df_new.to_sql("trades", conn, if_exists="append", index=False)
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