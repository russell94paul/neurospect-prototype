from pathlib import Path

# Updated base path
PROMPT_DIR = Path(__file__).parent.parent / 'agents' / 'prompts'

def load_prompt(category: str, version: str) -> str:
    """Load the prompt from prompts/<category>/<version>.txt"""
    path = PROMPT_DIR / category / f'{version}.txt'
    return path.read_text(encoding='utf-8')

def list_prompt_versions(category: str):
    """List all available prompt versions for a given category"""
    folder = PROMPT_DIR / category
    if not folder.exists():
        return []
    return [f.stem for f in folder.glob('*.txt')]