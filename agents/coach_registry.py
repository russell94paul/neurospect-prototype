from agents.psychology_coach import PsychologyCoach
from agents.risk_management_coach import RiskManagementCoach
from agents.narrative_coach import NarrativeCoach
from agents.execution_coach import ExecutionCoach
from agents.drill_sergeant_coach import DrillSergeantCoach
from agents.summary_coach import SummaryCoach
from agents.pattern_detection_coach import PatternDetectionCoach
from agents.setup_auditor_coach import SetupAuditorCoach
from agents.conviction_calibrator_coach import ConvictionCalibratorCoach

def get_registered_coaches():
    return {
        'Psychology Coach': PsychologyCoach,
        'Risk Management Coach': RiskManagementCoach,
        'Narrative Coach': NarrativeCoach,
        'Execution Coach': ExecutionCoach,
        'Drill Sergeant Coach': DrillSergeantCoach,
        'Summary Coach': SummaryCoach,
        'Pattern Detection Coach': PatternDetectionCoach,
        'Setup Auditor Coach': SetupAuditorCoach,
        'Conviction Calibrator Coach': ConvictionCalibratorCoach,
    }