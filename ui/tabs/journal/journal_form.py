from nicegui import ui

def render():
    print('[DEBUG] journal_form.render() called')
    
    with ui.card().classes('w-full max-w-3xl bg-[#1a1a2e] text-white shadow-md overflow-visible'):
        with ui.column().classes('p-6 gap-4'):
            ui.label('🧠 Structured Journal Form').classes('text-xl font-bold text-purple-400')
            ui.label('The core structured journaling form: bias, setup, emotion, confidence, risk, outcome.').classes('text-sm text-gray-400')

            # 🔧 Dummy filler content to test sticky tab bar
            ui.separator()
            ui.label('⬇️ Scroll to test sticky tab bar').classes('text-blue-400 italic')

            for i in range(50):
                ui.label(f'Placeholder line {i+1}: journal field simulation...').classes('text-sm text-gray-500')