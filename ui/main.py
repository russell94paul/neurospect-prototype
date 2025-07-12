from nicegui import ui
from tabs import (
    dashboard,
    journal,
    reports,
    self_review_lab,
    performance_lab,
    trade_doctor,
    drill_lab,
    setup_vault,
    social,
    settings
)

# -------- Global Routing State --------
current_tab = {'name': 'Home'}

# -------- Persistent Top Nav --------
def layout_shell():
    with ui.header().classes('bg-gray-900 text-white'):
        with ui.row().classes('items-center justify-between w-full p-4'):
            ui.label('🧠 NeuroSpect').classes('text-2xl font-bold')
            ui.label('Where beats are currency').classes('italic text-sm text-gray-300')
            ui.button(icon='account_circle').props('flat color=white')

# -------- Sidebar Navigation --------
def sidebar_nav():
    tab_labels = [
        'Home',
        'Dashboard',
        'Journal Your Trade',
        'Reports',
        'Self Review Lab',
        'Performance Lab',
        'Trade Doctor',
        'Drill Lab',
        'Setup Vault',
        'Social',
        'Settings'
    ]

    with ui.left_drawer().classes('bg-gray-800 text-white'):
        for label in tab_labels:
            ui.button(label, on_click=lambda l=label: switch_tab(l)).classes('w-full text-left')

# -------- Home Page w/ Tiles --------
def render_home():
    ui.label('🧠 Welcome to NeuroSpect').classes('text-2xl font-bold p-4')
    ui.label('Explore your tools and labs:').classes('p-2 text-sm text-gray-500')

    def tile(label, target):
        with ui.card().classes('w-64 m-2 cursor-pointer hover:shadow-lg'):
            ui.label(label).classes('text-lg font-bold p-4 text-center')
            ui.button('Open', on_click=lambda: switch_tab(target)).classes('mx-auto')

    for row in [
        [("📊 Dashboard", "Dashboard"), ("📓 Journal", "Journal Your Trade"), ("📅 Reports", "Reports")],
        [("🧠 Performance Lab", "Performance Lab"), ("🩺 Trade Doctor", "Trade Doctor"), ("🎯 Drill Lab", "Drill Lab")],
        [("🔐 Setup Vault", "Setup Vault"), ("👥 Social", "Social"), ("⚙️ Settings", "Settings")],
    ]:
        with ui.row().classes('p-2'):
            for label, key in row:
                tile(label, key)

# -------- Tab Dispatcher --------
def render_tab(tab_name):
    match tab_name:
        case 'Dashboard': dashboard.render()
        case 'Journal Your Trade': journal.render()
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
    current_tab['name'] = name
    ui.open('/')  # Reroute to main page

# -------- Main Page Routing --------
@ui.page('/')
def main_page():
    layout_shell()
    sidebar_nav()
    with ui.column().classes('p-4'):
        render_tab(current_tab['name'])

# -------- Run App --------
ui.run(title='NeuroSpect Dashboard', dark=True)