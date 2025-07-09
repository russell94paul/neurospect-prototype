import streamlit as st
from tabs.self_review_lab import bias_tracker, emotion_heatmap, mirror_mode, voice_journaling

def render():
    st.title("🧠 Self Review Lab")
    st.write("Use this space to reflect on recent trades through voice input, mirror exercises, and bias awareness tools.")

    with st.expander("🪞 Mirror Mode"):
        mirror_mode.render()

    with st.expander("🎯 Cognitive Bias Tracker"):
        bias_tracker.render()

    with st.expander("🗣️ Voice Journaling & Tone Scoring"):
        voice_journaling.render()

    with st.expander("🧠 Emotional Pattern Heatmap"):
        emotion_heatmap.render()