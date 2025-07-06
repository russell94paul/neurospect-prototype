import sys
import os
from pathlib import Path

# Add the project root to Python path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

import streamlit as st
from backend.storage import save_trade

# Elegant Dark Theme Configuration
st.set_page_config(
    page_title="NeuroSpect Trade Logger",
    page_icon="🧠",
    layout="wide"
)

# Modern Elegant Dark Theme CSS
st.markdown("""
<style>
    /* Import Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@300;400;500;600;700&family=Orbitron:wght@400;500;600;700;800;900&family=Inter:wght@300;400;500;600;700&display=swap');
    
    /* CSS Variables for Elegant Dark Theme */
    :root {
        --primary: #00d4aa;
        --primary-dark: #00b894;
        --primary-light: #00f5d4;
        --accent: #667eea;
        --accent-dark: #5a67d8;
        --dark-bg: #0a1428;
        --dark-surface: #1a2332;
        --dark-card: #1e2a3a;
        --dark-border: #2d3a4a;
        --text-primary: #ffffff;
        --text-secondary: #b0c4de;
        --text-muted: #7a8ba8;
        --success: #00d4aa;
        --error: #ff6b6b;
        --warning: #ffd93d;
    }
    
    /* Global Styles */
    * {
        font-family: 'JetBrains Mono', 'Inter', monospace;
    }
    
    /* Main App Background */
    .stApp {
        background: linear-gradient(135deg, var(--dark-bg) 0%, #1e2a3a 30%, #2d3a4a 70%, var(--dark-bg) 100%) !important;
        min-height: 100vh;
    }
    
    /* Container Styling */
    .block-container {
        background: rgba(30, 42, 58, 0.9) !important;
        backdrop-filter: blur(20px) !important;
        border: 1px solid rgba(255, 255, 255, 0.15) !important;
        border-radius: 20px !important;
        padding: 2.5rem !important;
        box-shadow: 0 25px 50px rgba(0, 0, 0, 0.4) !important;
        margin: 2rem auto !important;
        max-width: 1400px !important;
    }
    
    /* Header Styling */
    .main .block-container h1 {
        background: linear-gradient(135deg, var(--primary) 0%, var(--accent) 100%) !important;
        -webkit-background-clip: text !important;
        -webkit-text-fill-color: transparent !important;
        background-clip: text !important;
        font-family: 'Orbitron', monospace !important;
        font-size: 3.5rem !important;
        font-weight: 800 !important;
        text-align: center !important;
        margin-bottom: 3rem !important;
        letter-spacing: 0.1em !important;
        text-transform: uppercase !important;
        text-shadow: 0 0 30px rgba(0, 212, 170, 0.3) !important;
    }
    
    .main .block-container h2 {
        color: var(--text-primary) !important;
        font-family: 'Orbitron', monospace !important;
        font-size: 1.8rem !important;
        font-weight: 700 !important;
        margin-top: 2.5rem !important;
        margin-bottom: 1.5rem !important;
        padding-bottom: 0.75rem !important;
        border-bottom: 2px solid var(--primary) !important;
        position: relative !important;
        letter-spacing: 0.05em !important;
        text-transform: uppercase !important;
    }
    
    .main .block-container h2::after {
        content: '' !important;
        position: absolute !important;
        bottom: -2px !important;
        left: 0 !important;
        width: 50px !important;
        height: 2px !important;
        background: linear-gradient(90deg, var(--primary) 0%, var(--accent) 100%) !important;
    }
    
    /* Input Field Styling - Dark backgrounds */
    .stSelectbox > div > div,
    .stNumberInput > div > div,
    .stTextInput > div > div,
    .stTextArea > div > div,
    .stDateInput > div > div,
    .stTimeInput > div > div {
        background: rgba(255, 255, 255, 0.05) !important;
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
        border-radius: 12px !important;
        transition: all 0.3s ease !important;
        backdrop-filter: blur(10px) !important;
    }
    
    /* Force dark backgrounds for input elements */
    .stTextInput input,
    .stNumberInput input,
    .stTextArea textarea,
    .stDateInput input,
    .stTimeInput input {
        background-color: rgba(255, 255, 255, 0.05) !important;
        color: var(--text-primary) !important;
        border: none !important;
    }
    
    /* Override default input styling */
    input[type="text"],
    input[type="number"],
    input[type="date"],
    input[type="time"],
    textarea {
        background-color: rgba(255, 255, 255, 0.05) !important;
        color: var(--text-primary) !important;
        border: none !important;
    }
    
    /* Aggressive targeting for problematic fields */
    .stTextInput > div > div > div,
    .stNumberInput > div > div > div,
    .stTextArea > div > div > div,
    .stDateInput > div > div > div,
    .stTimeInput > div > div > div {
        background: rgba(255, 255, 255, 0.05) !important;
        backdrop-filter: blur(10px) !important;
    }
    
    /* Target the actual input containers */
    .stTextInput > div,
    .stNumberInput > div,
    .stTextArea > div,
    .stDateInput > div,
    .stTimeInput > div {
        background: rgba(255, 255, 255, 0.05) !important;
        backdrop-filter: blur(10px) !important;
    }
    
    /* Force all elements within input containers */
    .stTextInput *,
    .stNumberInput *,
    .stTextArea *,
    .stDateInput *,
    .stTimeInput * {
        background-color: rgba(255, 255, 255, 0.05) !important;
    }
    
    /* Use attribute selectors for maximum specificity */
    [data-testid="stTextInput"] > div,
    [data-testid="stNumberInput"] > div,
    [data-testid="stTextArea"] > div,
    [data-testid="stDateInput"] > div,
    [data-testid="stTimeInput"] > div {
        background: rgba(255, 255, 255, 0.05) !important;
        backdrop-filter: blur(10px) !important;
    }
    
    /* Nuclear option - target everything with high specificity */
    .stTextInput > div > div > div > div,
    .stNumberInput > div > div > div > div,
    .stTextArea > div > div > div > div,
    .stDateInput > div > div > div > div,
    .stTimeInput > div > div > div > div {
        background: rgba(255, 255, 255, 0.05) !important;
        backdrop-filter: blur(10px) !important;
    }
    
    /* Force dark backgrounds with !important and maximum specificity */
    .stTextInput input[type="text"],
    .stNumberInput input[type="number"],
    .stDateInput input[type="date"],
    .stTimeInput input[type="time"],
    .stTextArea textarea {
        background-color: rgba(255, 255, 255, 0.05) !important;
        color: var(--text-primary) !important;
        border: none !important;
        border-radius: 8px !important;
    }
    
    /* Alternative approach - target by class names that Streamlit actually uses */
    .stTextInput .stTextInput,
    .stNumberInput .stNumberInput,
    .stTextArea .stTextArea,
    .stDateInput .stDateInput,
    .stTimeInput .stTimeInput {
        background: rgba(255, 255, 255, 0.05) !important;
        backdrop-filter: blur(10px) !important;
    }
    
    /* Target any element with background-color property */
    [style*="background-color"] {
        background-color: rgba(255, 255, 255, 0.05) !important;
    }
    
    /* Final attempt - target the actual HTML elements Streamlit creates */
    div[data-baseweb="input"],
    div[data-baseweb="select"],
    div[data-baseweb="textarea"] {
        background: rgba(255, 255, 255, 0.05) !important;
        backdrop-filter: blur(10px) !important;
    }
    
    /* Override any remaining white backgrounds */
    *[style*="background: white"],
    *[style*="background-color: white"],
    *[style*="background: #ffffff"],
    *[style*="background-color: #ffffff"] {
        background: rgba(255, 255, 255, 0.05) !important;
    }
    
    /* Target specific problematic field types */
    .stDateInput input,
    .stNumberInput input,
    .stTextInput input,
    .stTextArea textarea {
        background-color: rgba(255, 255, 255, 0.05) !important;
        color: var(--text-primary) !important;
        border: none !important;
    }
    
    /* Number input buttons */
    .stNumberInput button {
        background-color: var(--dark-surface) !important;
        color: var(--text-primary) !important;
        border: 1px solid var(--primary) !important;
        border-radius: 4px !important;
    }
    
    .stNumberInput button:hover {
        background-color: var(--primary) !important;
        color: white !important;
    }
    
    .stSelectbox > div > div:hover,
    .stNumberInput > div > div:hover,
    .stTextInput > div > div:hover,
    .stTextArea > div > div:hover,
    .stDateInput > div > div:hover,
    .stTimeInput > div > div:hover {
        border-color: var(--primary) !important;
        box-shadow: 0 0 20px rgba(0, 212, 170, 0.2) !important;
    }
    
    .stSelectbox > div > div:focus-within,
    .stNumberInput > div > div:focus-within,
    .stTextInput > div > div:focus-within,
    .stTextArea > div > div:focus-within,
    .stDateInput > div > div:focus-within,
    .stTimeInput > div > div:focus-within {
        border-color: var(--primary) !important;
        box-shadow: 0 0 30px rgba(0, 212, 170, 0.3) !important;
        transform: translateY(-2px) !important;
    }
    
    /* Label Styling */
    .stSelectbox label, .stNumberInput label, .stTextInput label,
    .stTextArea label, .stDateInput label, .stTimeInput label {
        color: var(--text-primary) !important;
        font-family: 'JetBrains Mono', monospace !important;
        font-weight: 600 !important;
        font-size: 0.85rem !important;
        margin-bottom: 0.5rem !important;
        letter-spacing: 0.03em !important;
        text-transform: uppercase !important;
        opacity: 0.9 !important;
    }
    
    /* Button Styling */
    .stButton > button {
        background: linear-gradient(135deg, var(--primary) 0%, var(--primary-dark) 100%) !important;
        color: white !important;
        border: none !important;
        border-radius: 12px !important;
        padding: 0.75rem 2rem !important;
        font-family: 'Orbitron', monospace !important;
        font-weight: 700 !important;
        font-size: 1rem !important;
        transition: all 0.3s ease !important;
        box-shadow: 0 8px 25px rgba(0, 212, 170, 0.3) !important;
        letter-spacing: 0.05em !important;
        text-transform: uppercase !important;
    }
    
    .stButton > button:hover {
        background: linear-gradient(135deg, var(--primary-dark) 0%, var(--primary) 100%) !important;
        transform: translateY(-3px) !important;
        box-shadow: 0 12px 35px rgba(0, 212, 170, 0.4) !important;
    }
    
    /* Checkbox and Radio Styling */
    .stCheckbox > div > div,
    .stRadio > div > div {
        color: var(--text-primary) !important;
        font-family: 'JetBrains Mono', monospace !important;
        font-weight: 500 !important;
        font-size: 0.9rem !important;
        letter-spacing: 0.02em !important;
    }
    
    /* Success and Error Messages */
    .stSuccess {
        background: linear-gradient(135deg, var(--success) 0%, var(--primary-dark) 100%) !important;
        color: white !important;
        border: none !important;
        border-radius: 12px !important;
        padding: 1rem !important;
        font-family: 'Orbitron', monospace !important;
        font-weight: 600 !important;
        letter-spacing: 0.03em !important;
        text-transform: uppercase !important;
        box-shadow: 0 8px 25px rgba(0, 212, 170, 0.3) !important;
    }
    
    .stError {
        background: linear-gradient(135deg, var(--error) 0%, #ff5252 100%) !important;
        color: white !important;
        border: none !important;
        border-radius: 12px !important;
        padding: 1rem !important;
        font-family: 'Orbitron', monospace !important;
        font-weight: 600 !important;
        letter-spacing: 0.03em !important;
        text-transform: uppercase !important;
        box-shadow: 0 8px 25px rgba(255, 107, 107, 0.3) !important;
    }
    
    /* Column Spacing */
    .row-widget.stHorizontal {
        gap: 1.5rem !important;
    }
    
    /* Text Colors */
    .block-container p, .block-container div {
        color: var(--text-secondary) !important;
    }
    
    /* Scrollbar Styling */
    ::-webkit-scrollbar {
        width: 8px;
    }
    
    ::-webkit-scrollbar-track {
        background: var(--dark-surface);
    }
    
    ::-webkit-scrollbar-thumb {
        background: linear-gradient(180deg, var(--primary) 0%, var(--accent) 100%);
        border-radius: 4px;
    }
    
    ::-webkit-scrollbar-thumb:hover {
        background: linear-gradient(180deg, var(--primary-dark) 0%, var(--accent-dark) 100%);
    }
    
    /* Animation for page load */
    @keyframes fadeInUp {
        from {
            opacity: 0;
            transform: translateY(30px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    .block-container {
        animation: fadeInUp 0.6s ease-out;
    }
    
    /* Hover effects for interactive elements */
    .stSelectbox > div > div,
    .stNumberInput > div > div,
    .stTextInput > div > div,
    .stTextArea > div > div,
    .stDateInput > div > div,
    .stTimeInput > div > div {
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
    }
    
    /* Focus ring for accessibility */
    .stSelectbox > div > div:focus-within,
    .stNumberInput > div > div:focus-within,
    .stTextInput > div > div:focus-within,
    .stTextArea > div > div:focus-within,
    .stDateInput > div > div:focus-within,
    .stTimeInput > div > div:focus-within {
        outline: none !important;
        ring: 2px !important;
        ring-color: var(--primary) !important;
    }
</style>
""", unsafe_allow_html=True)

# App title at the top
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

st.markdown("## 🔹 Trade Execution Details")
col1, col2 = st.columns(2)

col1, col2 = st.columns(2)
trade_date = col1.date_input("Trade Date")
entry_time = col1.time_input("Entry Time")
exit_time = col2.time_input("Exit Time")
instrument = col2.selectbox("Instrument", ["MES", "ES", "NQ", "MNQ", "RTY", "Other"])
direction = st.selectbox("Entry Direction", ["Long", "Short"])
entry_type = st.selectbox("Entry Type", ["Reversal", "Continuation"])
risk_level = st.selectbox("Risk Level", ["Full", "Half"])
partial_exit = st.checkbox("Partial Exits Taken?")
profit_points = st.number_input("Profit (in points)", step=0.25)
execution_quality = st.selectbox("Execution Quality", ["Good", "Late", "Chased", "Hesitant"])
session = st.selectbox("Session", ["Asia", "London", "New York", "Crossover"])
news_today = st.text_input("News Events Today")


st.markdown("## 📊 Performance Context & Mindset")
account_type = st.selectbox("Account Type", ["Evaluation", "Funded", "Payout Phase", "Demo"])
drawdown_proximity = st.selectbox("Drawdown Proximity", ["No drawdown", "25%", "50%", "75%", "At limit"])
eval_progress = st.selectbox("Evaluation Progress", ["Start", "25%", "50%", "75%", "Close to pass"])
days_left = st.number_input("Days Left in Evaluation", min_value=0, step=1)
payout_proximity = st.selectbox("Payout Proximity", ["Just started", "2+ weeks", "Next week", "This week"])
sleep_quality = st.selectbox("Did you sleep well?", ["Yes", "Somewhat", "Poorly"])
caffeine = st.selectbox("Caffeine Intake", ["None", "Low", "Normal", "High"])
distractions = st.selectbox("Distractions while trading?", ["None", "Some", "High"])
meditated = st.checkbox("Meditated today?")
routine_done = st.checkbox("Followed routine?")
reviewed_plan = st.checkbox("Reviewed playbook before session?")
bias_prepped = st.checkbox("Had a pre-session bias?")
risk_today = st.selectbox("Risk per trade today", ["Full", "Half", "Micro", "Over-risked"])
matches_plan = st.selectbox("Trade matches strategy?", ["Yes", "Partial", "No"])
setup_grade = st.selectbox("Setup Grade", ["A+", "A", "B", "C"])
prep_time = st.selectbox("Prep Time Before Trading", ["None", "<15m", "15–30m", "30+m"])

st.markdown("## 🧠 Confluences & Notes")
notes = st.text_area("General Confluences / Notes")
emotionally_driven = st.checkbox("Was the trade emotionally driven?")
reflection = st.text_input("What would you do differently?")
screenshot_taken = st.checkbox("Screenshot Taken?")

# Storage Settings Section
st.markdown("## ⚙️ Storage Settings")
col1, col2, col3 = st.columns([1, 1, 1])
with col1:
    storage_mode = st.radio("Save trades to:", ["SQLite", "CSV"])

# Submit and Save to DB/CSV
if st.button("Submit Trade"):
    if direction and entry_type and trade_date:
        trade_data = {
            "trade_date": trade_date,
            "entry_time": entry_time,
            "exit_time": exit_time,
            "instrument": instrument,
            "direction": direction,
            "entry_type": entry_type,
            "risk_level": risk_level,
            "partial_exit": partial_exit,
            "profit_points": profit_points,
            "execution_quality": execution_quality,
            "session": session,
            "news_today": news_today,
            "account_type": account_type,
            "drawdown_proximity": drawdown_proximity,
            "eval_progress": eval_progress,
            "days_left": days_left,
            "payout_proximity": payout_proximity,
            "sleep_quality": sleep_quality,
            "caffeine": caffeine,
            "distractions": distractions,
            "meditated": meditated,
            "routine_done": routine_done,
            "reviewed_plan": reviewed_plan,
            "bias_prepped": bias_prepped,
            "risk_today": risk_today,
            "matches_plan": matches_plan,
            "setup_grade": setup_grade,
            "prep_time": prep_time,
            "notes": notes,
            "emotionally_driven": emotionally_driven,
            "reflection": reflection,
            "screenshot_taken": screenshot_taken,
        }
        
        save_trade(trade_data, mode=storage_mode.lower())
        st.success("✅ Trade logged successfully!")
    else:
        st.error("Please fill in all required fields.")