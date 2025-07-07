import streamlit as st
import pandas as pd
import json
from backend.storage import load_trades


def render_ai_feedback_block(trade):
    feedback_raw = trade.get("llm_feedback_json")

    if not feedback_raw:
        st.warning("⚠️ No LLM feedback found.")
        return

    # TEMP DEBUG OUTPUT
    #st.code(f"Raw JSON:\n{feedback_raw}", language="json")

    # Try parse
    try:
        if isinstance(feedback_raw, str):
            feedback = json.loads(feedback_raw)
        elif isinstance(feedback_raw, dict):
            feedback = feedback_raw
        else:
            raise ValueError("Unsupported feedback format type.")
    except Exception as e:
        st.error(f"⚠️ Failed to parse LLM feedback.\n{e}")
        return

    with st.expander("🧠 AI Coaching Feedback", expanded=False):
        st.markdown(f"**Setup Quality:** {feedback.get('setup_quality', '—')}")
        st.markdown(f"**Emotional Tone:** {feedback.get('emotional_tone', '—')}")
        st.markdown(f"**Risk Evaluation:** {feedback.get('risk_evaluation', '—')}")
        st.markdown(f"**Rationale:** {feedback.get('decision_rationale', '—')}")
        st.markdown(f"**Timing:** {feedback.get('timing_assessment', '—')}")
        st.markdown(f"**Bias Detected:** {feedback.get('bias_detected', '—')}")
        st.markdown(f"**Discipline Deviation:** {feedback.get('discipline_deviation', '—')}")
        st.markdown(f"**Plan Alignment:** {feedback.get('plan_alignment', '—')}")
        st.markdown(f"**Coaching Tip:** {feedback.get('coaching_tip', '—')}")
        st.markdown(f"**Self-Review Needed?** {'✅ Yes' if feedback.get('self_review_needed') else 'No'}")
        st.caption("🧠 GPT-generated coaching breakdown")


def render_view_trades(storage_mode="csv"):
    st.markdown("## 📘 View Past Trades")

    df = load_trades(storage_mode.lower())

    # Handle empty or invalid data
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

    st.markdown("---")
    st.markdown("### 🔍 Trade Coaching Breakdown")

    for _, trade in df.sort_values(by="trade_date", ascending=False).iterrows():
        with st.expander(f"🗓️ {trade['trade_date']} | {trade['instrument']} | {trade['direction']}"):
            st.markdown(f"**Profit Points:** {trade.get('profit_points', '—')}")
            st.markdown(f"**Execution Quality:** {trade.get('execution_quality', '—')}")
            st.markdown(f"**Setup Grade:** {trade.get('setup_grade', '—')}")
            st.markdown(f"**Reflection:** {trade.get('reflection', '—')}")
            render_ai_feedback_block(trade)