from nicegui import ui

# Reusable scrollable wrapper with styled scrollbar
def scroll_area(height: str = '100vh'):
    return ui.scroll_area().classes(
        f'overflow-y-auto w-full max-w-screen-xl mx-auto px-4 py-4 rounded-lg'  # full-width scroll area
    ).style(
        f'max-height: {height};'
    )
