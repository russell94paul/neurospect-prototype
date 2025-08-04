from agents.base import BaseCoach
from utils.prompts import load_prompt, list_prompt_versions
import json

class PatternDetectionCoach(BaseCoach):
    name = 'Pattern Detection'
    category = "pattern_detection"
    version = 'v1'
    prompt = load_prompt(category, version)

    def format_input(self, trade: dict) -> str:
        # Include only what’s available so far
        basic_fields = {
            "Market": trade.get("market"),
            "Session": trade.get("session"),
            "Datetime": trade.get("datetime"),
            "Bias": trade.get("ht_bias"),
            "Market Structure": trade.get("market_structure"),
            "Entry Method": trade.get("entry_method"),
            "Result": trade.get("result"),
            "Mental Notes": trade.get("mental_notes"),
            "Tags": trade.get("tags"),
        }

        return (
            "NOTE: This version uses a single trade as input. Pattern detection across trades will improve when multiple entries are processed.\n\n"
            f"Trade Input:\n{json.dumps(basic_fields, indent=2)}"
        )

    @classmethod
    def available_versions(cls) -> list[str]:
        return list_prompt_versions(cls.category)