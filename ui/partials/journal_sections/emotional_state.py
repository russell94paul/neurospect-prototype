from nicegui import ui

inputs = {}

def render():
    ui.label('🧠 Emotional & Cognitive State').classes('text-lg text-purple-300 font-semibold')
    ui.separator().classes('my-2')

    with ui.element('div').classes('flex flex-row gap-6 !flex-nowrap !items-start w-full'):

        # Left column
        with ui.element('div').classes('w-1/2 flex flex-col gap-4'):
            inputs['state_before'] = ui.select(
                ['Calm', 'Anxious', 'Excited', 'Focused', 'Tired', 'Irritated', 'Neutral'],
                label='Emotional State Before Trade'
            ).classes('w-full')

            # Caption + slider (no label kwarg on slider)
            with ui.element('div').classes('w-full flex flex-col gap-1'):
                ui.label('Confidence Level (0–10)').classes('text-sm text-gray-300')
                inputs['confidence_level'] = ui.slider(min=0, max=10, step=1, value=5).classes('w-full')
                inputs['confidence_level'].props('label-always')  # shows numeric value bubble

            inputs['state_after'] = ui.select(
                ['Relieved', 'Frustrated', 'Confident', 'Satisfied', 'Tilted', 'Calm', 'Disappointed', 'Neutral'],
                label='State After Trade'
            ).classes('w-full')

        # Right column
        with ui.element('div').classes('w-1/2 flex flex-col gap-4'):
            inputs['mindset_tags'] = ui.select(
                ['FOMO', 'Hesitant', 'Flow', 'Tilt', 'Greedy', 'Perfect Execution'],
                label='Mindset Tags',
                multiple=True
            ).classes('w-full')

            inputs['mental_notes'] = ui.textarea('Notes on Mental State').classes('w-full')


def get_data():
    # cast slider to int or None
    def _to_int(v):
        if v in (None, '', 'None'):
            return None
        try:
            return int(v)
        except Exception:
            return None

    return {
        'state_before': inputs['state_before'].value if 'state_before' in inputs else None,
        'confidence_level': _to_int(inputs['confidence_level'].value) if 'confidence_level' in inputs else None,
        'state_after': inputs['state_after'].value if 'state_after' in inputs else None,
        'mindset_tags': ','.join(inputs['mindset_tags'].value or []) if 'mindset_tags' in inputs else None,
        'mental_notes': inputs['mental_notes'].value if 'mental_notes' in inputs else None,
    }