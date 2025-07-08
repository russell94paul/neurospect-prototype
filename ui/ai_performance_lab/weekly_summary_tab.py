import os
import streamlit as st

SUMMARY_DIR = "."  # Set this to wherever the summary is saved
SUMMARY_FILENAME = None

# Auto-detect most recent summary file
def get_latest_summary_file():
    summaries = [f for f in os.listdir(SUMMARY_DIR) if f.startswith("weekly_summary_") and f.endswith(".md")]
    if not summaries:
        return None
    return max(summaries, key=lambda f: os.path.getmtime(os.path.join(SUMMARY_DIR, f)))

def render_weekly_summary():
    st.title("🧠 AI Performance Lab – Weekly Summary")

    global SUMMARY_FILENAME
    if not SUMMARY_FILENAME:
        SUMMARY_FILENAME = get_latest_summary_file()

    if not SUMMARY_FILENAME:
        st.warning("No weekly summary report found.")
        st.info("Run the summary generator from the backend or enable the button below.")
        return

    path = os.path.join(SUMMARY_DIR, SUMMARY_FILENAME)
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    st.markdown(f"### 📅 Summary File: `{SUMMARY_FILENAME}`", unsafe_allow_html=True)
    st.markdown("---")
    st.markdown(content, unsafe_allow_html=True)
    st.markdown("---")

    with open(path, "rb") as f:
        st.download_button(
            label="📥 Download Summary Markdown",
            data=f,
            file_name=SUMMARY_FILENAME,
            mime="text/markdown"
        )

    st.caption("Powered by GPT-3.5 via NeuroSpect")