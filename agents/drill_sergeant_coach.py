from agents.base import BaseCoach
from utils.prompts import load_prompt, list_prompt_versions

class DrillSergeantCoach(BaseCoach):
    name = 'Drill Sergeant'
    category = "drill_sergeant"
    version = 'v1'
    prompt = load_prompt('drill_sergeant', 'v1')
    
    @classmethod
    def available_versions(cls) -> list[str]:
        return list_prompt_versions(cls.name.lower())