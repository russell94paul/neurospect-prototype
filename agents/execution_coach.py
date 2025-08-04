from agents.base import BaseCoach
from utils.prompts import load_prompt, list_prompt_versions

class ExecutionCoach(BaseCoach):
    name = 'Execution'
    category = "execution"
    version = 'v1'
    prompt = load_prompt('execution', 'v1')
    
    @classmethod
    def available_versions(cls) -> list[str]:
        return list_prompt_versions(cls.name.lower())