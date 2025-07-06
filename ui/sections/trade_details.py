import streamlit as st
from datetime import datetime

def render_trade_execution_form():
    st.markdown("## 🔹 Trade Execution Details")
    col1, col2 = st.columns(2)

    with col1:
        trade_date = st.date_input("Trade Date", value=datetime.today())
        entry_time = st.time_input("Entry Time")
        direction = st.selectbox("Entry Direction", ["Long", "Short"])
        entry_type = st.selectbox("Entry Type", ["Reversal", "Continuation"])
        risk_level = st.number_input("Risk (Contracts)", step=1)
        partial_exit = st.checkbox("Partial Exits Taken?")
        profit_points = st.number_input("Profit (in points)", step=0.25)

    with col2:
        exit_time = st.time_input("Exit Time")
        instrument = st.selectbox("Instrument", ["MES", "ES", "NQ", "MNQ", "RTY", "Other"])
        execution_quality = st.selectbox("Execution Quality", ["Good", "Late", "Chased", "Hesitant"])
        session = st.selectbox("Session", ["Asia", "London", "New York", "Crossover"])
        news_today = st.text_input("News Events Today")

    return {
        "trade_date": trade_date,
        "entry_time": entry_time,
        "exit_time": exit_time,
        "instrument": instrument,
        "direction": direction,
        "entry_type": entry_type,
        "risk_level": risk_level,
        "partial_exit": partial_exit,
        "profit_points": profit_points,
        "execution_quality": execution_quality,
        "session": session,
        "news_today": news_today,
    }
