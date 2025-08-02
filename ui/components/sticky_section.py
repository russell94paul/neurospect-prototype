from nicegui import ui
from contextlib import contextmanager

# Inject styles only once
ui.add_head_html('''
<style>
.tab-button-wrapper {
    position: relative;
    display: flex;
    gap: 0.5rem;
}
.tab-button-wrapper .active-indicator {
    position: absolute;
    height: 4px;
    background: linear-gradient(to right, #8b5cf6, #3b82f6);
    border-radius: 2px;
    bottom: -6px;
    left: 0;
    width: 100px;
    transition: all 0.3s ease;
    transform: translateX(var(--active-tab-x, 0));
}
</style>
''')

@contextmanager
def sticky_section(tab_bar_function):
    """Sticky section for tab bar + heading that stays locked at top, with blur + animated tab underline."""

    # ✅ Sticky container (under header, translucent, blurred)
    with ui.element('div').classes(
        'sticky top-[88px] z-50 px-4 py-3 border-b border-zinc-800 backdrop-blur shadow-sm'
    ).style(
        'background-color: rgba(10, 10, 10, 0.65); will-change: transform;'
    ):
        tab_bar_function()

    # ✅ Content body follows (not inside scroll area)
    with ui.element('div').classes('px-6 py-6'):
        yield