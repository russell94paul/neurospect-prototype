from agents.base import BaseCoach
from utils.prompts import load_prompt, list_prompt_versions

class ConvictionCalibratorCoach(BaseCoach):
    name = 'Conviction Calibrator'
    category = "conviction_calibrator"
    version = 'v1'
    prompt = load_prompt('conviction_calibrator', 'v1')
    
    @classmethod
    def available_versions(cls) -> list[str]:
        return list_prompt_versions(cls.name.lower())