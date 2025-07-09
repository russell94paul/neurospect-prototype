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

# Tab Routing
tab_options = {
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

selected_tab = st.sidebar.selectbox("Navigation", list(tab_options.keys()))
tab_options[selected_tab]()