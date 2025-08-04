from pathlib import Path
from utils.openai_client import call_openai
from utils.prompts import load_prompt

class BaseCoach:
    category = 'base'  # must be overridden in subclasses

    def __init__(self, version='v1'):
        self.version = version
        self.prompt = load_prompt(self.category, version)

    def generate_feedback(self, trade: dict) -> str:
        input_text = self.format_input(trade)
        return call_openai(self.prompt, input_text)

    def format_input(self, trade: dict) -> str:
        raise NotImplementedError("format_input() must be implemented in subclass")