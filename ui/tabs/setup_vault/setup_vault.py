import streamlit as st
from ui.tabs.setup_vault import neurodna_summary, performance_overview, setup_templates, strategy_tracker

def render():
    st.title("🔐 Setup Vault")
    st.write("Your edge vault: store, tag, and track setup performance over time across market regimes.")

    with st.expander("🧬 NeuroDNA™ Summary"):
        neurodna_summary.render()

    with st.expander("🗂️ Setup Templates & Tags"):
        setup_templates.render()

    with st.expander("📊 Setup Performance Overview"):
        performance_overview.render()

    with st.expander("🧭 Strategy Tracker"):
        strategy_tracker.render()