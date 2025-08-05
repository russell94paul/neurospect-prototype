from agents.base import BaseCoach
from utils.prompts import load_prompt, list_prompt_versions

class SetupAuditorCoach(BaseCoach):
    name = 'Setup Auditor'
    category = "setup_auditor"
    version = 'v1'
    prompt = load_prompt('setup_auditor', 'v1')
    
    @classmethod
    def available_versions(cls) -> list[str]:
        return list_prompt_versions(cls.name.lower())