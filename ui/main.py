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
current_tab = {'name': 'Home'}

# -------- Persistent Top Nav --------
def layout_shell():
    with ui.header().classes('bg-[#101010] text-white shadow-md z-50'):
        with ui.row().classes('items-center justify-between w-full px-6 py-3'):
            ui.label('🧠 NeuroSpect').classes('text-2xl font-bold tracking-tight')
            ui.button(icon='account_circle').props('flat color=white').tooltip('Profile')

# -------- Sidebar Navigation --------
def sidebar_nav():
    tab_labels = [
        ('🏠 Home', 'Home'),
        ('📊 Dashboard', 'Dashboard'),
        ('📓 Journal', 'Journal Your Trade'),
        ('📅 Reports', 'Reports'),
        ('🧠 Self Review Lab', 'Self Review Lab'),
        ('🧪 Performance Lab', 'Performance Lab'),
        ('🩺 Trade Doctor', 'Trade Doctor'),
        ('🎯 Drill Lab', 'Drill Lab'),
        ('🔐 Setup Vault', 'Setup Vault'),
        ('👥 Social', 'Social'),
        ('⚙️ Settings', 'Settings'),
    ]

    with ui.left_drawer().classes('bg-[#151515] text-white pt-6'):
        for icon_label, name in tab_labels:
            ui.button(icon_label, on_click=lambda n=name: switch_tab(n)) \
                .classes('w-full justify-start text-left text-md font-semibold px-4 py-2 hover:bg-[#222] transition-all')

# -------- Home Page w/ Tiles --------
def render_home():
    with ui.row().classes('gap-8'):

        # -------- Left: Status Panels --------
        with ui.column().classes('w-1/2'):
            ui.label('🧠 NeuroSpect Command Center').classes('text-3xl font-bold text-white')
            ui.label('Track your state. Prep your edge. Execute clean.').classes('text-md text-gray-400 mb-4')

            def status_card(title, subtitle, icon):
                with ui.card().classes('w-full bg-[#1a1a1a] text-white mb-4 shadow-lg'):
                    with ui.row().classes('items-center justify-between px-4 py-2'):
                        with ui.column():
                            ui.label(title).classes('text-lg font-semibold')
                            ui.label(subtitle).classes('text-sm text-gray-400')
                        ui.icon(icon).classes('text-2xl text-blue-400')

            status_card("🧪 MindState: Optimal", "Focus good • Sleep solid", "psychology")
            status_card("🔥 Streak: 3W • Risk Zone: Safe", "Last: Clean scalp in NY Open", "trending_up")
            status_card("⚠️ Regime Warning", "Volatility Shift Detected", "warning")

        # -------- Right: Action Buttons --------
        with ui.column().classes('w-1/2'):
            ui.label('🚀 Quick Actions').classes('text-2xl font-semibold text-white mb-4')

            def action_group(title, items):
                ui.label(title).classes('text-md text-gray-400 mt-2 mb-1')
                with ui.row().classes('gap-2 flex-wrap'):
                    for icon_label, tab_key in items:
                        ui.button(icon_label, on_click=lambda t=tab_key: switch_tab(t)) \
                            .props('outline color=white') \
                            .classes('text-white border-white hover:bg-[#222] transition-all')

            action_group("Trade Workflow", [
                ("📓 Journal", "Journal Your Trade"),
                ("📅 Reports", "Reports"),
                ("📊 Dashboard", "Dashboard"),
            ])

            action_group("Mind & Review", [
                ("🧠 Self Review Lab", "Self Review Lab"),
                ("🧪 Performance Lab", "Performance Lab"),
                ("🩺 Trade Doctor", "Trade Doctor"),
            ])

            action_group("Tools & Settings", [
                ("🎯 Drill Lab", "Drill Lab"),
                ("🔐 Setup Vault", "Setup Vault"),
                ("👥 Social", "Social"),
                ("⚙️ Settings", "Settings"),
            ])

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
    ui.open('/')

# -------- Main Page Routing --------
@ui.page('/')
def main_page():
    layout_shell()
    sidebar_nav()
    with ui.column().classes('p-6 min-h-screen bg-[#0e0e0e]'):
        render_tab(current_tab['name'])

# -------- Run App --------
ui.run(title='NeuroSpect', dark=True)