from nicegui import ui

from tabs.dashboard import dashboard
from tabs.journal import journal
from tabs.reports import reports
from tabs.self_review_lab import self_review_lab
from tabs.performance_lab import performance_lab
from tabs.trade_doctor import trade_doctor
from tabs.drill_lab import drill_lab
from tabs.setup_vault import setup_vault
from tabs.social import social
from tabs.settings import settings

# -------- Global Routing State --------
current_tab = 'Home'

# -------- Persistent Top Nav --------
def layout_shell():
    with ui.header().classes('bg-[#101010] text-white shadow-md z-50'):
        with ui.row().classes('items-center justify-between w-full px-6 py-3'):
            ui.label('🧠 NeuroSpect').classes('text-2xl font-bold tracking-tight')
            ui.button(icon='account_circle').props('flat color=white').tooltip('Profile')

# -------- Header Navigation --------
def header_nav():
    with ui.header().classes('bg-[#101010] text-white shadow-md z-50'):
        with ui.row().classes('items-center justify-between w-full px-6 py-3'):

            # Left: Logo
            ui.label('🧠 NeuroSpect').classes('text-2xl font-bold tracking-widest text-purple-300')

            # Center: Navigation
            with ui.row().classes('gap-4'):
                nav_items = [
                    ("Journal", "Journal"),
                    ("Dashboard", "Dashboard"),
                    ("Labs", "Performance Lab"),
                    ("Reports", "Reports"),
                    ("Settings", "Settings"),
                ]
                for label, tab_key in nav_items:
                    ui.button(label, on_click=lambda k=tab_key: switch_tab(k)) \
                        .props('flat color=white') \
                        .classes('hover:text-purple-400 text-md transition')

            # Right: Profile
            ui.button(icon='account_circle').props('flat color=white').tooltip('Profile')

# -------- Home Layout --------
def render_home():
    with ui.column().classes('items-center text-white w-full gap-8'):

        # -- Neural Signals Panel --
        with ui.row().classes('w-full justify-around px-6 pt-6'):
            def signal_box(title, value, icon):
                with ui.card().classes('bg-gradient-to-br from-[#1a1a2e] to-[#16213e] text-white w-64 shadow-md hover:scale-105 transition'):
                    with ui.column().classes('p-4 items-start'):
                        ui.icon(icon).classes('text-blue-400 text-2xl')
                        ui.label(title).classes('text-sm text-gray-400')
                        ui.label(value).classes('text-xl font-bold text-purple-300')

            signal_box("MindScore", "7.8 / 10", "psychology")
            signal_box("Edge Sync", "82% Aligned", "bolt")
            signal_box("Regime", "High Volatility", "warning")

        # -- AI Summary Panel --
        with ui.card().classes('w-[80%] bg-[#111] text-white shadow-lg'):
            with ui.column().classes('p-6'):
                ui.label("🧠 AI Insight:").classes('text-lg font-semibold text-blue-300 pb-2')
                ui.label("“You’ve been most consistent when trading 10–20 minutes after NY open. Consider setting tighter risk today based on CPI volatility.”") \
                    .classes('text-md text-gray-300 italic')

        # -- Mission Control Grid --
        with ui.column().classes('w-[85%] items-center'):
            ui.label("🎯 Mission Control").classes('text-2xl font-bold text-purple-400 pb-2')

            def control_btn(label, tab_name, icon):
                ui.button(on_click=lambda: switch_tab(tab_name)) \
                    .classes('w-48 h-20 m-2 rounded-xl text-white bg-gradient-to-br from-[#1f1f38] to-[#161627] hover:from-purple-700 hover:to-blue-600 transition shadow-xl') \
                    .props(f'icon={icon} label="{label}"')

            with ui.row().classes('justify-center flex-wrap'):
                control_btn("Journal", "Journal", "note_alt")
                control_btn("Dashboard", "Dashboard", "dashboard")
                control_btn("Reports", "Reports", "insights")
                control_btn("Self Review Lab", "Self Review Lab", "psychology")
                control_btn("Performance Lab", "Performance Lab", "science")
                control_btn("Trade Doctor", "Trade Doctor", "healing")
                control_btn("Drill Lab", "Drill Lab", "sports_mma")
                control_btn("Setup Vault", "Setup Vault", "lock")
                control_btn("Social", "Social", "group")
                control_btn("Settings", "Settings", "settings")

# -------- Tab Dispatcher --------
def render_tab(tab_name):
    print(f"[DEBUG] render_tab() called with: {tab_name}")
    match tab_name:
        case 'Dashboard': dashboard.render()
        case 'Journal': 
            print("[DEBUG] matched 'Journal Your Trade' – calling journal.render()") 
            journal.render()
        case 'Reports': reports.render()
        case 'Self Review Lab': self_review_lab.render()
        case 'Performance Lab': performance_lab.render()
        case 'Trade Doctor': trade_doctor.render()
        case 'Drill Lab': drill_lab.render()
        case 'Setup Vault': setup_vault.render()
        case 'Social': social.render()
        case 'Settings': settings.render()
        case _: render_home()

# -------- Tab Switching Logic --------
def switch_tab(name):
    global current_tab
    print(f"[DEBUG] Switching to tab: {name}")
    current_tab = name
    page_body.refresh()

# -------- Refreshable Main Content --------
@ui.refreshable
def page_body():
    render_tab(current_tab)

# -------- Main Page Routing --------
@ui.page('/')
def main_page():
    # Inject global styling for font, scrollbars, layout fixes, and debug outlines
    ui.add_head_html('''
        <link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&display=swap" rel="stylesheet">
        <style>
        html, body {
            font-family: 'Orbitron', sans-serif;
            margin: 0;
            padding: 0;
            height: 100%;
            overflow-y: auto;
            background-color: #0a0a0a;
        }

        /* ✅ FIX: Remove Quasar layout interference */
        .q-page-container {
            padding-top: 0px !important;
        }
        .q-page {
            min-height: unset !important;
            overflow: visible !important;
        }

        /* Scrollbar styling */
        .custom-scroll::-webkit-scrollbar {
            width: 8px;
        }
        .custom-scroll::-webkit-scrollbar-thumb {
            background-color: #555;
            border-radius: 8px;
        }
        .custom-scroll::-webkit-scrollbar-track {
            background-color: #111;
        }
        .custom-scroll {
            scrollbar-width: thin;
            scrollbar-color: #555 #111;
        }

        /* ✅ DEBUG: Visual outlines to detect nested scrolls */
        html, body, .q-page, .q-page-container, .q-layout, .nicegui-content, .nicegui-page {
            outline: 2px dashed limegreen !important;
        }

        * {
            box-sizing: border-box;
        }
        </style>
    ''')

    # Top navigation bar outside scroll
    header_nav()

    # Scrollable content area
    with ui.element('div').classes('px-4 py-6 custom-scroll'):
        page_body()

# -------- Run App --------
ui.run(title='NeuroSpect', dark=True)