import streamlit as st

def render_storage_settings():
    st.markdown("## ⚙️ Storage Settings")
    col1, col2, col3 = st.columns([1, 1, 1])
    with col1:
        storage_mode = st.radio("Save trades to:", ["SQLite", "CSV"])
    return storage_mode