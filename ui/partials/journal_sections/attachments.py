from __future__ import annotations
import os
from datetime import datetime
from nicegui import ui, events

inputs = {}
_saved_paths = {}  # holds saved file paths per field

UPLOAD_DIR = os.path.join('data', 'uploads')  # relative to your project root


def _ensure_upload_dir():
    os.makedirs(UPLOAD_DIR, exist_ok=True)


def _unique_name(original: str) -> str:
    # prepend a timestamp to avoid collisions
    ts = datetime.now().strftime('%Y%m%d_%H%M%S_%f')
    base = os.path.basename(original or 'file')
    return f'{ts}__{base}'


def _save_bytes_to_disk(content: bytes, filename: str) -> str:
    _ensure_upload_dir()
    unique = _unique_name(filename)
    path = os.path.join(UPLOAD_DIR, unique)
    with open(path, 'wb') as f:
        f.write(content)
    return path


def _make_upload_row(label: str, field: str, accept: str | None = None):
    """Creates an upload control + readonly path display + clear button."""
    with ui.row().classes('w-full items-center gap-3'):
        # Upload button
        def _on_upload(e: events.UploadEvent):
            try:
                path = _save_bytes_to_disk(e.content.read() if hasattr(e.content, 'read') else e.content, e.name)
                _saved_paths[field] = path
                inputs[field].value = path
                ui.notify(f'{label} saved', type='positive')
            except Exception as ex:
                ui.notify(f'Failed to save {label}: {ex}', type='negative')

        uploader = ui.upload(label=f'Upload {label}', on_upload=_on_upload)
        if accept:
            uploader.props(f'accept={accept}')

        # Readonly path display
        inputs[field] = ui.input(f'{label} Path').props('readonly').classes('w-full')

        # Clear button
        def _clear():
            _saved_paths[field] = None
            inputs[field].value = ''
        ui.button('Clear', on_click=_clear).props('flat').classes('text-sm')


def render():
    ui.label('📎 Attachments').classes('text-lg text-purple-300 font-semibold')
    ui.separator().classes('my-2')

    with ui.element('div').classes('flex flex-row gap-6 !flex-nowrap !items-start w-full'):

        # Left column
        with ui.element('div').classes('w-1/2 flex flex-col gap-4'):
            _make_upload_row('Entry Screenshot', 'entry_screenshot', accept='image/*')
            _make_upload_row('Footprint Snapshot', 'footprint_snapshot', accept='image/*')
            _make_upload_row('Volume/MP Chart', 'volume_mp_chart', accept='image/*')

        # Right column
        with ui.element('div').classes('w-1/2 flex flex-col gap-4'):
            _make_upload_row('Audio Commentary', 'audio_commentary', accept='audio/*')
            _make_upload_row('OF/DOM Log Snippet', 'of_dom_log', accept='.txt,.log,application/json,text/plain')


def get_data():
    # Return the file paths (or None/empty if not provided)
    def _val(key):
        # prefer saved path registry (what we wrote to disk), else input value
        v = _saved_paths.get(key)
        if v:
            return v
        if key in inputs and getattr(inputs[key], 'value', None):
            return inputs[key].value
        return None

    return {
        'entry_screenshot': _val('entry_screenshot'),
        'footprint_snapshot': _val('footprint_snapshot'),
        'volume_mp_chart': _val('volume_mp_chart'),
        'audio_commentary': _val('audio_commentary'),
        'of_dom_log': _val('of_dom_log'),
    }