import sys
import os
from pathlib import Path
import streamlit as st

from tabs.journal import journal
from tabs.dashboard import dashboard
from tabs.reports import reports
from tabs.self_review_lab import self_review_lab
from tabs.performance_lab import performance_lab
from tabs.trade_doctor import trade_doctor
from tabs.drill_lab import drill_lab
from tabs.setup_vault import setup_vault
from tabs.social import social
from tabs.settings import settings



# Add project root to Python path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

st.set_page_config(page_title="NeuroSpect", layout="wide")

def render_home():
    st.title("🧠 Welcome to NeuroSpect")
    st.write("Explore your tools and labs:")

    def tile(label, key):
        st.markdown(f"""
            <div style='
                background-color: #1e1e1e;
                padding: 2rem;
                border-radius: 15px;
                text-align: center;
                font-size: 1.1rem;
                font-weight: bold;
                cursor: pointer;
                transition: 0.3s ease;
                border: 2px solid #444;
            '
            onClick="document.getElementById('{key}').click()"
            onmouseover="this.style.backgroundColor='#333'"
            onmouseout="this.style.backgroundColor='#1e1e1e'"
            >
                {label}
            </div>
        """, unsafe_allow_html=True)
        st.button(" ", key=key)  # invisible button to trigger routing

    cols = st.columns(3)
    with cols[0]: tile("📊 Dashboard", "goto_dashboard")
    with cols[1]: tile("📓 Journal", "goto_journal")
    with cols[2]: tile("📅 Reports", "goto_reports")

    cols = st.columns(3)
    with cols[0]: tile("🧠 Performance Lab", "goto_performance")
    with cols[1]: tile("🩺 Trade Doctor", "goto_doctor")
    with cols[2]: tile("🎯 Drill Lab", "goto_drills")

    cols = st.columns(3)
    with cols[0]: tile("🔐 Setup Vault", "goto_vault")
    with cols[1]: tile("👥 Social", "goto_social")
    with cols[2]: tile("⚙️ Settings", "goto_settings")


# Handle tile button clicks
mapping = {
    "goto_dashboard": "Dashboard",
    "goto_journal": "Journal Your Trade",
    "goto_reports": "Reports",
    "goto_performance": "Performance Lab",
    "goto_doctor": "Trade Doctor",
    "goto_drills": "Drill Lab",
    "goto_vault": "Setup Vault",
    "goto_social": "Social",
    "goto_settings": "Settings",
}

for key, tab in mapping.items():
    if st.session_state.get(key):
        st.session_state.selected_tab = tab
        st.rerun()


# Tab Routing
tab_options = {
    "Home": None,  # will be handled manually
    "Dashboard": dashboard.render,
    "Journal Your Trade": journal.render,
    "Reports": reports.render,
    "Self Review Lab": self_review_lab.render,
    "Performance Lab": performance_lab.render,
    "Trade Doctor": trade_doctor.render,
    "Drill Lab": drill_lab.render,
    "Setup Vault": setup_vault.render,
    "Social": social.render,
    "Settings": settings.render,
}

if "selected_tab" not in st.session_state:
    st.session_state.selected_tab = "Home"

selected_tab = st.sidebar.selectbox("Navigation", list(tab_options.keys()), index=list(tab_options).index(st.session_state.selected_tab))


if selected_tab == "Home":
    render_home()
else:
    tab_options[selected_tab]()