import os
import json
import openai
import logging
from tenacity import retry, wait_random_exponential, stop_after_attempt
from typing import Dict, Any

# Load your OpenAI API key from the environment
openai.api_key = os.getenv("OPENAI_API_KEY")

# Logging setup
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logfile = os.path.join("data", "llm_logs.jsonl")
os.makedirs("data", exist_ok=True)

# -------------------------
# Prompt Builder Class
# -------------------------

class TradeFeedbackPrompt:
    SYSTEM_PROMPT = (
        "You are a professional trading performance coach. Analyze the trade based on strategy, notes, preparation, "
        "risk, execution, emotional state, and account pressure. Respond ONLY in strict JSON using these keys:\n\n"
        "- setup_quality: A short assessment of how technically sound the setup was.\n"
        "- emotional_tone: Describe the trader’s state of mind (e.g., calm, hesitant, anxious, aggressive).\n"
        "- risk_evaluation: Was the use of risk appropriate given the setup and conviction?\n"
        "- decision_rationale: Does the reasoning in the notes justify the trade?\n"
        "- timing_assessment: Was the entry early, late, or ideal relative to price action?\n"
        "- bias_detected: Identify any cognitive bias (e.g., confirmation bias, revenge, overconfidence, FOMO). If none, say 'None'.\n"
        "- discipline_deviation: Did this trade appear to break the trader's plan or system rules? (Yes, No, Unknown)\n"
        "- plan_alignment: Did the execution align with the stated idea or notes?\n"
        "- coaching_tip: One short, specific improvement suggestion.\n"
        "- self_review_needed: Boolean. True if this trade warrants further review.\n\n"
        "Respond ONLY with the JSON object. Do not include any explanation or markdown."
    )

    def __init__(self, trade_data: Dict[str, Any]):
        self.trade = trade_data
        
    @staticmethod
    def _make_json_safe(obj):
        """Make all values safe for JSON encoding."""
        if isinstance(obj, (int, float, bool)) or obj is None:
            return obj
        if isinstance(obj, str):
            return obj.strip() if obj.strip() else "N/A"
        if isinstance(obj, (list, tuple)):
            return [TradeFeedbackPrompt._make_json_safe(i) for i in obj] or "N/A"
        if isinstance(obj, dict):
            return {str(k): TradeFeedbackPrompt._make_json_safe(v) for k, v in obj.items()} or "N/A"
        if hasattr(obj, "isoformat"):
            return obj.isoformat()
        return str(obj)

    def format_user_message(self) -> str:
        """Generate a consistent, deterministic JSON string for the GPT prompt."""
        fields_to_include = [
            "trade_date", "direction", "entry_type", "risk_level", "execution_quality", "profit_points", "session",
            "account_type", "drawdown_proximity", "payout_proximity", "eval_progress", "days_left", "emotionally_driven",
            "emotional_regulation", "routine_done", "reviewed_plan", "bias_prepped", "risk_today", "matches_plan",
            "setup_grade", "prep_time", "sleep_quality", "caffeine", "distractions", "notes", "reflection"
        ]
        filtered = {
            k: self._make_json_safe(self.trade.get(k, "N/A"))
            for k in sorted(fields_to_include)
        }
        return json.dumps(filtered, indent=2, sort_keys=True)


# -------------------------
# GPT Feedback Retrieval
# -------------------------

@retry(wait=wait_random_exponential(min=1, max=40), stop=stop_after_attempt(3))
def get_trade_feedback(trade_data: Dict[str, Any]) -> Dict[str, Any]:
    prompt = TradeFeedbackPrompt(trade_data)

    try:
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            temperature=0.0,
            messages=[
                {"role": "system", "content": prompt.SYSTEM_PROMPT},
                {"role": "user", "content": prompt.format_user_message()}
            ]
        )
        content = response.choices[0].message.content
        if content is None:
            raise ValueError("No content received from OpenAI API")
        feedback = json.loads(content)

        # Optional: Add raw feedback summary string
        trade_data["llm_feedback_json"] = feedback
        trade_data["llm_feedback_summary"] = feedback.get("setup_quality", "")[:100]

        _log_prompt_and_response(prompt, feedback)
        return feedback

    except Exception as e:
        logger.exception("❌ GPT feedback generation failed.")
        return {
            "setup_quality": "N/A",
            "emotional_tone": "N/A",
            "risk_evaluation": "N/A",
            "decision_rationale": "N/A",
            "timing_assessment": "N/A",
            "bias_detected": "N/A",
            "discipline_deviation": "N/A",
            "plan_alignment": "N/A",
            "coaching_tip": "N/A",
            "self_review_needed": False
        }


# -------------------------
# Log for Fine-Tuning / QA
# -------------------------

def _log_prompt_and_response(prompt: TradeFeedbackPrompt, response: Dict[str, Any]):
    try:
        with open(logfile, "a") as f:
            f.write(json.dumps({
                "prompt": json.loads(prompt.format_user_message()),
                "response": response
            }) + "\n")
    except Exception as e:
        logger.warning(f"⚠️ Failed to log LLM prompt/response: {e}")