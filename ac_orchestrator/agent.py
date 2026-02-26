from google.adk.agents.llm_agent import Agent
from ac_orchestrator.tools.ac_tools import control_ac
import time


def classify_intent(user_input: str) -> dict:
    text = user_input.lower()

    ac_keywords = [
        "ac",
        "temperature",
        "turn on",
        "turn off",
        "increase",
        "decrease",
        "cold",
        "hot",
    ]

    is_ac = any(word in text for word in ac_keywords)

    return {"is_ac_command": is_ac}


root_agent = Agent(
    name="ac_orchestrator",
    model="claude-3-5-sonnet-20241022",  # 🔥 CHANGED TO CLAUDE
    description="AC control orchestration agent.",
    instruction="""
You are a smart AC controller.

Step 1:
Call classify_intent(user_input).

If is_ac_command is false:
Return:
{
  "status": "false",
  "message": "Not an AC command"
}

If is_ac_command is true:
Call control_ac(action, value)

Allowed actions:
TURN_ON
TURN_OFF
SET_TEMP
INCREASE_TEMP
DECREASE_TEMP

If user says:
"I feel cold" → INCREASE_TEMP by 2
"I feel hot" → DECREASE_TEMP by 2

You MUST call tools properly.
""",
    tools=[classify_intent, control_ac],
)