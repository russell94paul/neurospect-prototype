
import sys
import os
from pathlib import Path
import streamlit as st

# Add project root to Python path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

# Streamlit config
st.set_page_config(
    page_title="NeuroSpect Trade Logger",
    page_icon="🧠",
    layout="wide"
)

# === Import UI Sections ===
from ui.sections.header import render_header
from ui.sections.trade_details import render_trade_execution_form
from ui.sections.perfomance_context import performance_context_ui
from ui.sections.notes import render_notes_section
from ui.sections.storage_settings import render_storage_settings
from ui.sections.submit import render_submit_button

from ui.view_trades import render_view_trades
from ui.screenshots import upload_screenshots

# === Page Setup ===
render_header()

# === Collect Input Sections ===
trade_data = {}  # Empty dict to hold all user input

# Section: Trade Execution
trade_data.update(render_trade_execution_form())

# Section: Performance Context & Mindset
trade_data.update(performance_context_ui())

# Section: Notes & Reflection
trade_data.update(render_notes_section())

# Section: Upload Screenshots
uploaded_image_paths = upload_screenshots()
trade_data["screenshots"] = uploaded_image_paths

# Section: Storage Preference
storage_mode = render_storage_settings()

# Final Submission
render_submit_button(trade_data, storage_mode)

# Section: View Trades
st.markdown("---")
render_view_trades(storage_mode)