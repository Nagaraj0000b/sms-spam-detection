from typing import Dict,TypedDict,List
from langchain_core.messages import HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.graph import StateGraph,START,END
from dotenv import load_dotenv

load_dotenv()


class AgentState(TypedDict):
    message:List[HumanMessage]
    
    
llm=ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite",temperature=0)


def chat_node(state:AgentState)->AgentState:
    response=llm.invoke(state['message'])
    print("AI : " + response.content)
    return state

graph=StateGraph(AgentState)
graph.add_node("chat",chat_node)
graph.add_edge(START,"chat")
graph.add_edge("chat",END)
app=graph.compile()

user_input=input("You : ")
while user_input!="exit":
    answer=app.invoke({"message":[HumanMessage(content=user_input)]})
    user_input=input("You : ")
