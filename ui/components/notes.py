import streamlit as st

def render_notes_section():
    st.markdown("## 🧠 Confluences & Notes")
    
    notes = st.text_area("General Confluences / Notes")
    emotionally_driven = st.checkbox("Was the trade emotionally driven?")
    reflection = st.text_input("What would you do differently?")
    screenshot_taken = st.checkbox("Screenshot Taken?")

    return {
        "notes": notes,
        "emotionally_driven": emotionally_driven,
        "reflection": reflection,
        "screenshot_taken": screenshot_taken
    }