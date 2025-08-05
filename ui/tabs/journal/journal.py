from nicegui import ui
from ui.components.sticky_section import sticky_section

from ui.tabs.journal import (
    journal_form,
    screenshots,
    trade_feedback,
    tradeflex_generator,
    export_to_mirror_toggle,
    audio_debrief,
    view_trades,
)

# Full tab metadata with icons
tab_config = [
    {"label": "Journal Form", "key": "form", "icon": "note_alt"},
    {"label": "Screenshots", "key": "shots", "icon": "photo"},
    {"label": "AI Feedback", "key": "feedback", "icon": "insights"},
    {"label": "TradeFlex Generator", "key": "generator", "icon": "memory"},
    {"label": "Export to Mirror", "key": "mirror", "icon": "sync"},
    {"label": "Audio Debrief", "key": "audio", "icon": "mic"},
    {"label": "View Past Trades", "key": "view", "icon": "folder"},
]

def render():
    selected_index = {"value": 0}

    def render_tab_content(index: int):
        selected_index["value"] = index
        key = tab_config[index]["key"]

        # Content is rendered here based on selected tab
        match key:
            case "form":
                journal_form.render()
            case "shots":
                screenshots.render()
            case "feedback":
                trade_feedback.render()
            case "generator":
                tradeflex_generator.render()
            case "mirror":
                export_to_mirror_toggle.render()
            case "audio":
                audio_debrief.render()
            case "view":
                view_trades.render()

    # Call sticky_section with full config (icons included)
    sticky_section(tab_config, on_tab_change=render_tab_content, default_index=selected_index["value"])