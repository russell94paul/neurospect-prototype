from pathlib import Path
import pandas as pd
import sqlite3
import os

# Define centralized paths
DATA_DIR = Path(__file__).parent.parent / "data"
CSV_PATH = DATA_DIR / "trade_log.csv"
DB_PATH = DATA_DIR / "trades.db"

# Ensure the data folder exists
DATA_DIR.mkdir(parents=True, exist_ok=True)

def save_trade(trade_data: dict, mode="csv"):
    if mode == "csv":
        df = pd.DataFrame([trade_data])
        if CSV_PATH.exists():
            df.to_csv(CSV_PATH, mode='a', header=False, index=False)
        else:
            df.to_csv(CSV_PATH, index=False)
    elif mode == "sqlite":
        conn = sqlite3.connect(DB_PATH)
        df = pd.DataFrame([trade_data])
        df.to_sql("trades", conn, if_exists="append", index=False)
        conn.close()
        
def load_trades(mode="csv"):
    if mode == "csv":
        if not CSV_PATH.exists():
            return pd.DataFrame()
        return pd.read_csv(CSV_PATH)
    
    elif mode == "sqlite":
        if not DB_PATH.exists():
            return pd.DataFrame()
        return pd.read_sql("SELECT * FROM trades", sqlite3.connect(DB_PATH))

    else:
        raise ValueError(f"Unsupported storage mode: {mode}")