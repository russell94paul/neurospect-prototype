import streamlit as st
from tabs.social import accountability_ping, share_reports, comment_threads

def render():
    st.title("👥 Social & Discord")
    st.write("Connect with the NeuroSpect community and stay accountable through social integrations.")

    with st.expander("🔔 Accountability Ping"):
        accountability_ping.render()

    with st.expander("📤 Share Reports"):
        share_reports.render()

    with st.expander("🧵 Comment Threads"):
        comment_threads.render()