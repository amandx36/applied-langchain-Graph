from langchain_community.chat_models import ChatOllama
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage

llm = ChatOllama(
    model="tinyllama:latest",  
    temperature=0.7
)


chat_history = [
    SystemMessage(content="You are a helpful and very knowledgeable assistant. Answer the question as best as you can politely.")
]

while True:

    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Good bye take care !!")
        break

    # adding user message to chat history
    chat_history.append(HumanMessage(content=user_input))

    # invoking model with full chat history 
    response = llm.invoke(chat_history)

    print("Bot:", response.content)
    
    # adding AI response to chat history
    chat_history.append(AIMessage(content=response.content))

    
    
print("Chat history is this :", chat_history)