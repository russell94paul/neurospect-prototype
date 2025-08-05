from nicegui import ui

from ui.tabs.dashboard import dashboard
from ui.tabs.journal import journal
from ui.tabs.reports import reports
from ui.tabs.self_review_lab import self_review_lab
from ui.tabs.performance_lab import performance_lab
from ui.tabs.trade_doctor import trade_doctor
from ui.tabs.drill_lab import drill_lab
from ui.tabs.setup_vault import setup_vault
from ui.tabs.social import social
from ui.tabs.settings import settings

# -------- Global Routing State --------
current_tab = 'Home'

# -------- Header Navigation --------
def header_nav():
    with ui.header().classes('bg-[#101010] text-white shadow-md z-50'):
        with ui.row().classes('items-center justify-between w-full px-6 py-3'):
            ui.label('🧠 NeuroSpect').classes('text-2xl font-bold tracking-widest text-purple-300')
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
            ui.button(icon='account_circle').props('flat color=white').tooltip('Profile')

# -------- Tab Dispatcher --------
def render_tab(tab_name):
    match tab_name:
        case 'Dashboard': dashboard.render()
        case 'Journal': journal.render()
        case 'Reports': reports.render()
        case 'Self Review Lab': self_review_lab.render()
        case 'Performance Lab': performance_lab.render()
        case 'Trade Doctor': trade_doctor.render()
        case 'Drill Lab': drill_lab.render()
        case 'Setup Vault': setup_vault.render()
        case 'Social': social.render()
        case 'Settings': settings.render()
        case _: render_home()

# -------- Home Layout --------
def render_home():
    with ui.column().classes('items-center text-white w-full gap-8'):
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

        with ui.card().classes('w-[80%] bg-[#111] text-white shadow-lg'):
            with ui.column().classes('p-6'):
                ui.label("🧠 AI Insight:").classes('text-lg font-semibold text-blue-300 pb-2')
                ui.label("“You’ve been most consistent when trading 10–20 minutes after NY open. Consider setting tighter risk today based on CPI volatility.”") \
                    .classes('text-md text-gray-300 italic')

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

# -------- Tab Switching Logic --------
def switch_tab(name):
    global current_tab
    current_tab = name
    page_body.refresh()

# -------- Refreshable Main Content --------
@ui.refreshable
def page_body():
    render_tab(current_tab)

# -------- Main App Route — Redirect to Landing --------
from fastapi.responses import RedirectResponse

@ui.page('/')
def redirect_to_landing():
    return RedirectResponse('/landing')

# -------- App Shell Layout --------
@ui.page('/app')
def main_page():
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
            .q-page-container {
                padding-top: 0px !important;
            }
            .q-page {
                min-height: unset !important;
                overflow: visible !important;
            }
        </style>
    ''')
    header_nav()
    with ui.element('div').classes('px-4 py-6'):
        page_body()

# -------- Redirect for Start Journaling Button --------
@ui.page('/journal')
def redirect_to_journal_tab():
    switch_tab('Journal')
    main_page()

# -------- Landing Page --------
@ui.page('/landing')
def landing_page():
    ui.add_head_html('''
        <link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&display=swap" rel="stylesheet">
        <style>
            html, body {
                font-family: 'Orbitron', sans-serif;
                background-color: #0a0a0a;
                margin: 0;
                padding: 0;
                overflow: hidden;
            }
            .landing-wrapper {
                position: relative;
                height: 100vh;
                width: 100vw;
                display: flex;
                justify-content: center;
                align-items: center;
                z-index: 1;
            }
            .glow-card {
                background: #1f1b2e;
                padding: 5rem 7rem;
                border-radius: 2rem;
                text-align: center;
                box-shadow: 0 0 45px #9333ea88, 0 0 100px #9333ea55;
                animation: pulse 2.5s infinite ease-in-out;
                max-width: 1000px;
                width: 90%;
            }
            @keyframes pulse {
                0%, 100% {
                    box-shadow: 0 0 45px #9333ea88, 0 0 100px #9333ea55;
                }
                50% {
                    box-shadow: 0 0 65px #a855f788, 0 0 120px #a855f766;
                }
            }
            .title {
                font-size: 3.5rem;
                color: #e9d5ff;
                text-shadow: 0 0 12px #c084fc;
                animation: fadeInUp 1s ease-out forwards;
            }
            .tagline {
                color: #e0e0e0;
                margin-top: 1rem;
                font-size: 1.2rem;
                animation: fadeInUp 1.2s ease-out 0.3s forwards;
                opacity: 0;
            }
            .button-purple {
                margin-top: 2.5rem;
                padding: 1rem 2.5rem;
                border-radius: 12px;
                border: 2px solid #a855f7;
                color: #e9d5ff;
                background-color: transparent;
                font-size: 1.1rem;
                cursor: pointer;
                transition: all 0.3s ease;
                display: inline-block;
            }
            .button-purple:hover {
                background-color: #a855f7;
                color: #0a0a0a;
                box-shadow: 0 0 16px #a855f7;
            }
            .prototype-link {
                display: block;
                margin-top: 1.8rem;
                color: #60a5fa;
                font-size: 1rem;
                text-decoration: none;
                transition: color 0.3s ease;
            }
            .prototype-link:hover {
                color: #93c5fd;
            }
            @keyframes fadeInUp {
                0% { opacity: 0; transform: translateY(20px); }
                100% { opacity: 1; transform: translateY(0); }
            }
            canvas#bgCanvas {
                position: fixed;
                top: 0;
                left: 0;
                width: 100%;
                height: 100%;
                z-index: 0;
            }
        </style>
    ''')

    # Particle background
    ui.add_body_html('''
        <canvas id="bgCanvas"></canvas>
        <script>
            const canvas = document.getElementById('bgCanvas');
            const ctx = canvas.getContext('2d');
            function resize() {
                canvas.width = window.innerWidth;
                canvas.height = window.innerHeight;
            }
            window.addEventListener('resize', resize);
            resize();
            const stars = Array.from({ length: 150 }, () => ({
                x: Math.random() * canvas.width,
                y: Math.random() * canvas.height,
                radius: 1.5 + Math.random() * 2.5,
                dx: (Math.random() - 0.5) * 0.4,
                dy: (Math.random() - 0.5) * 0.4,
                alpha: 0.6 + Math.random() * 0.4,
            }));
            function draw() {
                ctx.clearRect(0, 0, canvas.width, canvas.height);
                for (const star of stars) {
                    ctx.beginPath();
                    ctx.arc(star.x, star.y, star.radius, 0, 2 * Math.PI);
                    ctx.fillStyle = `rgba(216, 145, 255, ${star.alpha})`;
                    ctx.shadowBlur = 10;
                    ctx.shadowColor = '#e9d5ff';
                    ctx.fill();
                    star.x += star.dx;
                    star.y += star.dy;
                    if (star.x < 0 || star.x > canvas.width) star.dx *= -1;
                    if (star.y < 0 || star.y > canvas.height) star.dy *= -1;
                }
                requestAnimationFrame(draw);
            }
            draw();
        </script>
    ''')

    with ui.element('div').classes('landing-wrapper'):
        with ui.element('div').classes('glow-card'):
            ui.label('NeuroSpect').classes('title')
            ui.label('Behavioral Feedback for Elite Traders').classes('tagline')
            ui.html('<a href="/journal" class="button-purple">Start Journaling</a>')
            ui.html('<a class="prototype-link" href="/app">View Full Prototype →</a>')

# -------- Run App --------
ui.run(title='NeuroSpect',port=8080, dark=True)