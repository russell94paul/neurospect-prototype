import streamlit as st
from ui.tabs.settings import global_account_switcher, account_manager, storage_settings

def render():
    st.title("⚙️ Settings")
    st.write("Configure your trading accounts, default views, and data storage preferences.")

    with st.expander("🌍 Global Account Switcher"):
        global_account_switcher.render()

    with st.expander("🧾 Account Manager"):
        account_manager.render()

    with st.expander("💾 Storage Settings"):
        storage_settings.render()