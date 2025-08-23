from typing import Dict,TypedDict,List, Union
from langchain_core.messages import HumanMessage,AIMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.graph import StateGraph,START,END
from dotenv import load_dotenv
import os

load_dotenv()


class AgentState(TypedDict):
    message:List[Union[HumanMessage,AIMessage]]


llm=ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite",temperature=0)


def chat_node(state:AgentState)->AgentState:
    response=llm.invoke(state['message'])
    state['message'].append(AIMessage(content=response.content))
    print("AI : " + response.content)
    return state

graph=StateGraph(AgentState)
graph.add_node("chat",chat_node)
graph.add_edge(START,"chat")
graph.add_edge("chat",END)
app=graph.compile()

# Load previous conversation from logging.txt if exists
conversation_history=[]
if os.path.exists("logging.txt"):
    with open("logging.txt", "r") as file:
        for line in file:
            if line.startswith("You: "):
                content = line[len("You: "):].strip()
                conversation_history.append(HumanMessage(content=content))
            elif line.startswith("AI: "):
                content = line[len("AI: "):].strip()
                conversation_history.append(AIMessage(content=content))

# To read previous conversation from logging.txt
# if os.path.exists("logging.txt"):
#     with open("logging.txt", "r") as file:
#         previous_log = file.read()
#         # print(previous_log)

user_input=input("You : ")
while user_input!="exit":
    conversation_history.append(HumanMessage(content=user_input))
    # If conversation exceeds 10 messages, remove the oldest
    if len(conversation_history) > 20:
        conversation_history.pop(0)
    answer=app.invoke({"message":conversation_history})
    conversation_history=answer['message']
    # If conversation exceeds 20 messages after AI response, remove the oldest
    if len(conversation_history) > 20:
        conversation_history.pop(0)
    user_input=input("You : ")



with open("logging.txt", "w") as file:
    file.write("Your Conversation Log:\n")
    
    for message in conversation_history:
        if isinstance(message, HumanMessage):
            file.write(f"You: {message.content}\n")
        elif isinstance(message, AIMessage):
            file.write(f"AI: {message.content}\n\n")
    file.write("End of Conversation")

print("Conversation saved to logging.txt")