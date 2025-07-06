import streamlit as st
import pandas as pd
from backend.storage import load_trades

def render_view_trades(storage_mode="sqlite"):
    st.markdown("## 📘 View Past Trades")

    df = load_trades(storage_mode.lower())
    
    # Ensure df is a pandas DataFrame and handle empty case
    if df is None or (isinstance(df, pd.DataFrame) and df.empty):
        st.info("No trades logged yet.")
        return
    elif not isinstance(df, pd.DataFrame):
        df = pd.DataFrame(df)



    with st.expander("📅 Filter Options"):
        date_filter = st.date_input("Filter by trade date (optional)", [])
        instrument_filter = st.multiselect("Instrument", options=df['instrument'].unique())
        direction_filter = st.multiselect("Direction", options=df['direction'].unique())

        if date_filter:
            df = df[df['trade_date'].isin(pd.to_datetime(date_filter).tolist())]
        if instrument_filter:
            df = df[df['instrument'].isin(instrument_filter).tolist()]
        if direction_filter:
            df = df[df['direction'].isin(direction_filter).tolist()]

    st.dataframe(df.sort_values(by="trade_date", ascending=False), use_container_width=True)