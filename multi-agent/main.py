from agents import Agent, Runner
from dotenv import load_dotenv
import chainlit as cl

load_dotenv()

# ===========================================
webDeveloper = Agent(
    model="gpt-4.1-nano",
    name="webDev_agent",
    instructions="you will handel all web development related inquries.provide clear information about website issues.",
    handoff_description="you are an expert in web development issue."
)
    
mobileAppDeveloper = Agent(
    model="gpt-4.1-nano",
    name="mobileDev_agent",
    instructions="you will handle all mobile app development issues.",
    handoff_description="you are an expert in mobile app."
)

marketingAgent = Agent(
    model="gpt-4.1-nano",
    name="marketer_agent",
    instructions="you are handle all markteing issue",
    handoff_description="you are an expert in marketing issues."
)
triage = Agent(
    model="gpt-4.1-nano",
    name="triage",
    instructions="you delegate task to appropriate agents according to user input.",
    handoffs=[webDeveloper,mobileAppDeveloper,marketingAgent]
)
@cl.on_message
async def chat(message:cl.Message):
    user_chat = message.content
    

    result=  Runner.run_sync(triage, input=user_chat)
    await cl.Message(content=result.final_output).send()

# print(result.final_output)
# print(result._last_agent.name)

