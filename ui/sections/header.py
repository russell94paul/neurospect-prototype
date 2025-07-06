import streamlit as st

def render_header():
    st.markdown("""
    <div style='text-align: center;'>
      <h1 style='
        margin-top: 25px; margin-bottom: 0;
        font-family: Orbitron, monospace;
        font-size: 3.5rem; font-weight: 800;
        letter-spacing: 0.1em; text-transform: uppercase;
        background: linear-gradient(135deg, #00d4aa 0%, #667eea 100%);
        -webkit-background-clip: text; -webkit-text-fill-color: transparent;
        background-clip: text; text-shadow: 0 0 30px rgba(0, 212, 170, 0.3);
        border-bottom: 4px solid #00d4aa; padding-bottom: 0.2em;
        display: inline-block;
      '>NeuroSpect</h1>
      <h1 style='
        margin-top: 0;
        font-family: Orbitron, monospace;
        font-size: 2rem; font-weight: 700;
        letter-spacing: 0.08em; text-transform: uppercase;
        background: linear-gradient(135deg, #00d4aa 0%, #667eea 100%);
        -webkit-background-clip: text; -webkit-text-fill-color: transparent;
        background-clip: text; text-shadow: 0 0 20px rgba(0, 212, 170, 0.2);
      '>Journal Your Trade</h1>
    </div>
    """, unsafe_allow_html=True)