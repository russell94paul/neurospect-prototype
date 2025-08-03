import streamlit as st
from ui.tabs.reports import weekly_summary, monthly_summary, yearly_summary

def render():
    st.title("📊 Reports")
    st.write("Access AI-generated trade summaries across weekly, monthly, and yearly timeframes.")

    with st.expander("📅 Weekly Summary"):
        weekly_summary.render()

    with st.expander("🗓️ Monthly Summary"):
        monthly_summary.render()

    with st.expander("📆 Yearly Summary"):
        yearly_summary.render()