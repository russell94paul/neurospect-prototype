from nicegui import ui
from data.db import get_all_trades
from ui.components.trade_detail import render_trade_detail


def render():
    ui.add_head_html('''
        <style>
            .expansion-glow {
                transition: all 0.3s ease;
                box-shadow: 0 0 12px 2px rgba(168,85,247,0.3);
                border-radius: 0.75rem;
            }

            .expansion-glow:hover {
                box-shadow: 0 0 20px 4px rgba(168,85,247,0.5);
            }

            .q-expansion__content {
                transition-property: max-height, opacity;
                transition-duration: 1.4s, 1.4s;
                transition-delay: 0.05s, 0.05s;
                overflow: hidden;
                opacity: 0;
            }

            .q-expansion--expanded .q-expansion__content {
                opacity: 1;
            }

            .q-expansion__toggle-icon {
                transition: transform 0.6s ease;
            }

            .r-cell {
                font-family: monospace;
                font-weight: bold;
                text-align: right;
                padding-right: 12px;
                border-radius: 6px;
            }
            .r-low {
                color: #f87171;
            }
            .r-mid {
                color: #facc15;
            }
            .r-high {
                color: #34d399;
                text-shadow: 0 0 4px rgba(52,211,153,0.6);
            }

            .custom-row {
                display: grid;
                grid-template-columns: repeat(9, 1fr);
                gap: 0.75rem;
                padding: 0.75rem 1rem;
                align-items: center;
                min-height: 48px;
            }

            .custom-header {
                font-weight: 700;
                background-color: #1a1a2e;
                border-bottom: 1px solid rgba(255, 255, 255, 0.05);
            }

            .custom-body {
                background-color: #1f1f35;
                border-bottom: 1px solid rgba(255, 255, 255, 0.05);
                transition: background-color 0.2s ease-in-out;
            }

            .custom-body:nth-child(even) {
                background-color: #1a1a2e;
            }

            .custom-body:hover {
                background-color: rgba(168, 85, 247, 0.1);
                box-shadow: 0 0 8px rgba(168, 85, 247, 0.2);
            }

            .custom-cell {
                font-size: 0.875rem;
                line-height: 1.25rem;
                word-break: break-word;
                font-family: 'Orbitron', sans-serif;
            }

            .text-left {
                text-align: left;
            }

            .text-right {
                text-align: right;
            }
        </style>
    ''')

    with ui.column().classes('w-full max-w-7xl mx-auto'):
        ui.label('📘 Trade History').classes('text-2xl font-bold mb-4 text-purple-300')

        trades = get_all_trades() or []

        with ui.element('div').classes(
            'transition-all duration-300 hover:shadow-[0_0_20px_4px_rgba(168,85,247,0.5)] '
            'shadow-[0_0_12px_2px_rgba(168,85,247,0.3)] ring-1 ring-purple-500/30 rounded-xl mb-6'
        ):
            with ui.card().classes('w-full bg-[#1a1a2e] text-white rounded-xl'):
                # Header row
                with ui.element('div').classes('custom-row custom-header text-white'):
                    for label in ['Date', 'Market', 'Session', 'Bias', 'Exec Ctx', 'Result', 'R', 'Grade', 'Setup']:
                        align = 'text-right' if label == 'R' else 'text-left'
                        with ui.element('div').classes(f'custom-cell {align}'):
                            ui.html(label)

                # Data rows
                for trade in trades:
                    r = trade.get('r_multiple', 0)
                    r_class = 'r-low' if r < 1 else 'r-mid' if r < 2 else 'r-high'
                    r_html = f'<span class="r-cell {r_class}">{r:.2f}</span>'

                    with ui.element('div').classes('custom-row custom-body text-white'):
                        def cell(value, align='text-left'):
                            with ui.element('div').classes(f'custom-cell {align}'):
                                ui.html(value)

                        cell(trade.get('datetime') or '—')
                        cell(trade.get('market') or '—')
                        cell(trade.get('session') or '—')
                        cell(trade.get('ht_bias') or '—')
                        cell(trade.get('execution_context') or '—')
                        cell(trade.get('result') or '—')
                        cell(r_html, align='text-right')  # R column right-aligned
                        cell(trade.get('grade') or '—')
                        cell(trade.get('setup_label') or '—')

        ui.separator().classes('my-4')

        # Expansion cards
        for trade in trades:
            date = trade.get('datetime') or '—'
            market = trade.get('market') or '—'
            session = trade.get('session') or '—'
            result = trade.get('result') or '—'
            r_mult = f"{trade.get('r_multiple'):.2f}" if isinstance(trade.get('r_multiple'), (int, float)) else (trade.get('r_multiple') or '—')
            grade = trade.get('grade') or '—'
            setup = trade.get('setup_label') or ''

            header = f"{date} – {market} – {session} | {result} | R {r_mult} | {grade} – {setup}"

            with ui.element('div').classes('w-full max-w-7xl mx-auto expansion-glow mb-4'):
                with ui.card().classes('w-full bg-[#1a1a2e] text-white rounded-xl'):
                    with ui.expansion(header) \
                        .props('switch-toggle-side') \
                        .classes('w-full transition-all duration-700 ease-in-out text-white') \
                        .style('''
                            --q-expansion-icon-color: #a855f7;
                            --q-expansion-icon-hover-color: #d946ef;
                        '''):
                        render_trade_detail(trade)