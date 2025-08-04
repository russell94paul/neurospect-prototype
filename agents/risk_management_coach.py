from agents.base import BaseCoach
from utils.prompts import load_prompt, list_prompt_versions

class RiskManagementCoach(BaseCoach):
    name = 'Risk Management'
    category = "risk_management"
    version = 'v1'
    prompt = load_prompt('risk_management', 'v1')
    
    @classmethod
    def available_versions(cls) -> list[str]:
        return list_prompt_versions(cls.name.lower())