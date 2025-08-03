from nicegui import ui
from ui.tabs.dashboard import (
    trader_performance_index,
    mindscore_widget,
    neurostreaks,
    regime_warning,
    next_tasks,
    heatmap_calendar,
    account_breakdown_card,
    toggle_global_vs_active
)

def render():
    # Title and subtitle
    ui.label('📊 Dashboard').classes('text-2xl font-bold mb-1')
    ui.label('This is your real-time trader control panel. Review your performance, mindset, and edge alignment at a glance.').classes('text-sm text-gray-500 mb-4')

    # Each section uses a collapsible panel
    with ui.expansion('📈 Trader Performance Index (TPI)', icon='show_chart').classes('w-full'):
        trader_performance_index.render()

    with ui.expansion('🧠 MindScore™, Sleep & Stress', icon='psychology').classes('w-full'):
        mindscore_widget.render()

    with ui.expansion('🔥 Live NeuroStreaks™', icon='whatshot').classes('w-full'):
        neurostreaks.render()

    with ui.expansion('⚠️ Regime Warning', icon='warning').classes('w-full'):
        regime_warning.render()

    with ui.expansion('🧪 Next Prompt / Drill / Review Task', icon='science').classes('w-full'):
        next_tasks.render()

    with ui.expansion('🗓️ Heatmap Calendar', icon='calendar_month').classes('w-full'):
        heatmap_calendar.render()

    with ui.expansion('🥧 Account Breakdown Card', icon='pie_chart').classes('w-full'):
        account_breakdown_card.render()

    with ui.expansion('🔄 Global vs Active Account Toggle', icon='sync').classes('w-full'):
        toggle_global_vs_active.render()