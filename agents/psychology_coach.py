from agents.base import BaseCoach
from utils.prompts import load_prompt, list_prompt_versions
import json

class PsychologyCoach(BaseCoach):
    name = 'Psychology'
    category = 'psychology'

    def __init__(self, version='v1'):
        self.version = version
        self.prompt = load_prompt(self.category, version)

    def format_input(self, trade: dict) -> str:
        psych_fields = {
            "State Before": trade.get("state_before"),
            "Confidence Level": trade.get("confidence_level"),
            "State After": trade.get("state_after"),
            "Mindset Tags": trade.get("mindset_tags"),
            "Mental Notes": trade.get("mental_notes"),
            "Result": trade.get("result"),
            "Followed Plan": bool(trade.get("followed_plan")),
            "Grade": trade.get("grade"),
            "What Went Well": trade.get("what_went_well"),
            "What Needs Improvement": trade.get("what_needs_improvement"),
        }

        return (
            "The following journaled trade includes the trader’s psychological context and reflections.\n"
            "Use this information to analyze mindset patterns, mental performance, and provide targeted feedback.\n\n"
            f"Trade Psychology Snapshot:\n{json.dumps(psych_fields, indent=2)}"
        )

    def generate_feedback(self, trade: dict) -> str:
        """Single-trade feedback used by coach_feedback.py."""
        input_text = self.format_input(trade)
        return self.run(input_text)

    @classmethod
    def available_versions(cls) -> list[str]:
        return list_prompt_versions(cls.category)