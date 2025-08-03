import streamlit as st
from ui.tabs.performance_lab import spia, amrp, setup_consistency, bias_accuracy, execution_quality, decision_friction

def render():
    st.title("📊 Performance Lab")
    st.write("This tab provides agents and analysis tools to help you improve core aspects of your trading execution.")

    with st.expander("🧠 SPIA (Strategy Performance Improvement Agent)"):
        spia.render()

    with st.expander("📈 AMRP (Adaptive Market Regime Profiler)"):
        amrp.render()

    with st.expander("🎯 Setup Consistency Engine"):
        setup_consistency.render()

    with st.expander("📊 Bias Accuracy Lab"):
        bias_accuracy.render()

    with st.expander("💥 Execution Quality Analysis"):
        execution_quality.render()

    with st.expander("🧩 Decision Friction Score"):
        decision_friction.render()