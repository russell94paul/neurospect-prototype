import sqlite3
import pandas as pd
import os

def save_trade(trade_data: dict, mode: str = "sqlite"):
    if mode == "sqlite":
        conn = sqlite3.connect("trade_log.db")
        df = pd.DataFrame([trade_data])
        df.to_sql("trades", conn, if_exists="append", index=False)
        conn.close()

    elif mode == "csv":
        df = pd.DataFrame([trade_data])
        file_exists = os.path.isfile("trade_log.csv")
        df.to_csv("data/trade_log.csv", mode='a', header=not file_exists, index=False)

    else:
        raise ValueError(f"Unknown storage mode: {mode}")