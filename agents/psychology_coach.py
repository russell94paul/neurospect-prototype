from agents.base import BaseCoach

class PsychologyCoach(BaseCoach):
    category = 'psychology'

    def format_input(self, trade: dict) -> str:
        return (
            f"Emotional State Before: {trade.get('state_before', '-')}\n"
            f"Confidence Level: {trade.get('confidence_level', '-')}\n"
            f"Emotional State After: {trade.get('state_after', '-')}\n"
            f"Mental Notes: {trade.get('mental_notes', '-')}\n"
            f"Mindset Tags: {trade.get('mindset_tags', '-')}"
        )