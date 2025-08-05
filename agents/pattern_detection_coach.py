from agents.base import BaseCoach
from utils.prompts import load_prompt, list_prompt_versions
import json

class PatternDetectionCoach(BaseCoach):
    name = 'Pattern Detection'
    category = 'pattern_detection'

    def __init__(self, version='v2'):
        prompt = load_prompt(self.category, version)
        super().__init__()
        self.version = version
        self.prompt = prompt

    def format_input(self, trades: list[dict]) -> str:
        """
        Format the entire trade history into a JSON structure suitable for deep behavioral analysis.
        Each trade will include both operational and emotional fields.
        """
        relevant_fields = [
            "datetime", "market", "session", "ht_bias",
            "execution_context", "setup_label", "result", "r_multiple",
            "grade", "state_before", "state_after", "confidence_level",
            "mindset_tags", "mental_notes", "followed_plan",
            "what_went_well", "what_needs_improvement"
        ]

        trimmed_trades = [
            {key: trade.get(key) for key in relevant_fields}
            for trade in trades
        ]

        return (
            "Analyze the trader’s behavior using the following full journal history. "
            "Each trade includes execution details and emotional/cognitive context.\n\n"
            f"Trade Journal History:\n{json.dumps(trimmed_trades, indent=2)}"
        )

    @classmethod
    def available_versions(cls) -> list[str]:
        return list_prompt_versions(cls.category)