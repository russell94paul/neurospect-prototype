import streamlit as st
from tabs.journal import (
    journal_form,
    screenshots,
    trade_feedback,
    tradeflex_generator,
    export_to_mirror_toggle,
    audio_debrief,
    view_trades
)

def render():
    st.title("📓 Journal Your Trade")
    st.write("Log your trades in a structured format, get AI feedback, and track emotional patterns.")

    with st.expander("📝 Trade Journal Form"):
        journal_form.render()

    with st.expander("📷 Screenshots"):
        screenshots.render()

    with st.expander("📊 AI Trade Feedback"):
        trade_feedback.render()

    with st.expander("🧱 TradeFlex Card Generator"):
        tradeflex_generator.render()

    with st.expander("🔄 Export to Mirror Mode"):
        export_to_mirror_toggle.render()

    with st.expander("🎤 Audio Debrief & Tone Analysis"):
        audio_debrief.render()

    with st.expander("🗂️ View Past Trades"):
        view_trades.render()