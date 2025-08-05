import streamlit as st
from ui.tabs.trade_doctor import error_tree, xray_mode, recovery_plan, classification_tags

def render():
    st.title("🩺 Trade Doctor")
    st.write("Use this tab for focused corrective feedback. Diagnose what went wrong and how to fix it.")

    with st.expander("🌳 Cause of Error Tree"):
        error_tree.render()

    with st.expander("🔬 X-Ray Mode"):
        xray_mode.render()

    with st.expander("🛠️ AI Recovery Plan"):
        recovery_plan.render()

    with st.expander("🏷️ Trade Classification Tags"):
        classification_tags.render()