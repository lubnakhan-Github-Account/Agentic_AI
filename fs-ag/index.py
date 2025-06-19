from dataclasses import dataclass
from agents import Agent, Runner, function_tool,RunContextWrapper
from dotenv import load_dotenv
import rich


load_dotenv()
# ------------------------------------
# it is "context" code


@dataclass
class User_info():
    name:str
    age:int
    address:str

information= User_info("John", 21, "NewYark")
#------------------------------------------
@function_tool
async def get_info(wrapper:RunContextWrapper[User_info])-> str:
    return f" user name is {wrapper.context.name} and age is {wrapper.context.age} and address is {wrapper.context.address}"


agent = Agent[User_info](
       name="my agent",
       instructions="you are a helpful assistent.",
       model="gpt-4.1-nano",
       tools=[get_info]
   )
result= Runner.run_sync(agent,"tell me user name and age?",context=information)
rich.print(result)