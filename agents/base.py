from pathlib import Path
from utils.openai_client import call_openai

class BaseCoach:
    category = 'base'  # must be overridden in subclasses

    def __init__(self, version='v1'):
        self.version = version
        self.prompt = self.load_prompt(version)

    def load_prompt(self, version: str) -> str:
        prompt_path = Path(__file__).parent.parent / 'prompts' / self.category / f'{version}.txt'
        return prompt_path.read_text(encoding='utf-8')

    def generate_feedback(self, trade: dict) -> str:
        input_text = self.format_input(trade)
        return call_openai(self.prompt, input_text)

    def format_input(self, trade: dict) -> str:
        raise NotImplementedError("format_input() must be implemented in subclass")