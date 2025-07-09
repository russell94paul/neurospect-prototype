import streamlit as st
from tabs.dashboard import (
    trader_performance_index,
    mindscore_widget,
    neurostreaks,
    regime_warning,
    next_tasks,
    heatmap_calendar,
    account_breakdown_card,
    toggle_global_vs_active
)

def render():
    st.title("📊 Dashboard")
    st.write("This is your real-time trader control panel. Review your performance, mindset, and edge alignment at a glance.")

    with st.expander("📈 Trader Performance Index (TPI)"):
        trader_performance_index.render()

    with st.expander("🧠 MindScore™, Sleep & Stress"):
        mindscore_widget.render()

    with st.expander("🔥 Live NeuroStreaks™"):
        neurostreaks.render()

    with st.expander("⚠️ Regime Warning"):
        regime_warning.render()

    with st.expander("🧪 Next Prompt / Drill / Review Task"):
        next_tasks.render()

    with st.expander("🗓️ Heatmap Calendar"):
        heatmap_calendar.render()

    with st.expander("🥧 Account Breakdown Card"):
        account_breakdown_card.render()

    with st.expander("🔄 Global vs Active Account Toggle"):
        toggle_global_vs_active.render()