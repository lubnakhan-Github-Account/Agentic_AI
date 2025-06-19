from agents import Agent, Runner, function_tool 
from dotenv import load_dotenv
import rich

load_dotenv()

# --------------------------------------------------
# it is "function as tool" code.
# --------------------------------------------------
@function_tool
def weatherFunc():
    """it is a function as tool to pass an agent."""
    print("todays weather of  sawat")
    
# ---------------------------------------------------
agent= Agent(
    model="gpt-4.1-nano",
    name="func-agent",
    instructions="you are a helpful assistent.",
    tools=[weatherFunc]
)
#-------------------------------------------------------------
res= Runner.run_sync(agent,"what is the weather of lahore?")
rich.print(res) 
