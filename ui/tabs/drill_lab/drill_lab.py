import streamlit as st
from tabs.drill_lab import drills

def render():
    st.title("🎯 Drill Lab")
    st.write("Mental and execution drills to help automate edge behavior and internalize discipline.")

    with st.expander("🧪 Skill Drills"):
        drills.render()