from utils.openai_client import call_openai

class BaseCoach:
    category = 'base'  # must be overridden in subclasses
    prompt = None      # must be set in subclass
    version = 'v1'     # default version

    def run(self, input_text: str) -> str:
        """Call the OpenAI client with the coach's prompt and formatted input."""
        if self.prompt is None:
            raise ValueError("Prompt not set on coach instance.")

        return call_openai(
            prompt=self.prompt,
            input_text=input_text
        )

    def format_input(self, trade_or_trades) -> str:
        raise NotImplementedError("format_input() must be implemented in subclass.")