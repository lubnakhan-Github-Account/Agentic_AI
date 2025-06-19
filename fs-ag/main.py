from agents import Agent, FileSearchTool, Runner
from dotenv import load_dotenv

# ---------------------------------------
# it is "file search as tool" code.

load_dotenv()

agent= Agent(
    model="gpt-4.1-mini",
    name="f-agent",
    instructions="you are a helpful assistent.",
    tools=[FileSearchTool(
        max_num_results=3,
        vector_store_ids=["vs_684dde77b0ac81918e8985b9681c0214"]
    )]
    
)
res= Runner.run_sync(agent,"what is uid?")
print(res.final_output)