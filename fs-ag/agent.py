from agents import Agent,Runner
from dotenv import load_dotenv
import rich

load_dotenv()
# ------------------------------------------------
# it is "agent as tool" code.

poet_agent= Agent(
    name="poet_agent",
    instructions="you are an expert in poetry.",
    model="gpt-4.1-nano"
)
triage_agent= Agent(
    name="test-agent",
    instructions="you are a helpful assistent.",
    model="gpt-4.1-nano",
    tools=[poet_agent.as_tool(tool_name="poet_agent",tool_description="you are expert in poetry.")],
)
# --------------------------------------------------------------------------------------------------
result= Runner.run_sync(triage_agent,"poetry about flower in 1 line.")
rich.print(result.final_output)