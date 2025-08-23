from typing import Dict,TypedDict,Annotated,Sequence
from dotenv import load_dotenv
from langchain_core.messages import BaseMessage,ToolMessage,SystemMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.tools import tool
from langgraph.graph import StateGraph,START,END
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode


load_dotenv()

class AgentState(TypedDict):
    messages: Annotated[Sequence[BaseMessage],add_messages]
    
    
@tool
def add(a:int,b:int):
    """Adds two numbers.

    Args:
        a (int): The first number.
        b (int): The second number.
    """
    return a+b

@tool
def subtract(a:int,b:int):
    """Subtracts two numbers.

    Args:
        a (int): The first number.
        b (int): The second number.
    """
    return a-b

@tool
def multiply(a:int,b:int):
    """Multiplies two numbers.

    Args:
        a (int): The first number.
        b (int): The second number.
    """
    return a*b

@tool
def divide(a:int,b:int):
    """Divides two numbers.

    Args:
        a (int): The first number.
        b (int): The second number.
    """
    if b == 0:
        return "Division by zero error"
    return a/b

tools=[add,subtract,multiply,divide]

model=ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite").bind_tools(tools)


def chat_node(state:AgentState)->AgentState:
    system_prompt=SystemMessage(
        content="You are my AI assistant, please help me with my tasks."
    )
    response=model.invoke([system_prompt]+state['messages'])
    return{"messages":[response]}

def should_continue(state:AgentState):
    messages=state['messages']
    last_message=messages[-1]
    if not last_message.tool_calls:
        return "end"
    else:
        return "continue"
    
graph=StateGraph(AgentState)

graph.add_node("our_agent",chat_node)
tool_node=ToolNode(tools=tools)
graph.add_node("tools",tool_node)

graph.set_entry_point("our_agent")
graph.add_conditional_edges(
    "our_agent",should_continue,
    {
        "continue":"tools",
        "end":END
    }
)

graph.add_edge("tools","our_agent")

app=graph.compile()

def print_stream(stream):
    """Prints the messages from the stream.

    Args:
        stream (iterable): The stream of messages.
    """
    for s in stream:
        message=s["messages"][-1]
        if  isinstance(message,tuple):
            print(message)
        else:
          message.pretty_print()

inputs={"messages":[("user","add 40+12 ")]}
print_stream(app.stream(inputs,stream_mode="values"))