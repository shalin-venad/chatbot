from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

template = """
You are a helpful AI assistant.

{context}
User: {question}
AI:"""

model = OllamaLLM(model="MODEL_NAME") //add your model
prompt = ChatPromptTemplate.from_template(template)

chain = prompt | model

def convo():
    context = ""
    print("Welcome to AI Chatbot , type bye to exit")
    while True:
        user = input("User: ")
        if user.lower() == "bye":
            break
        result = chain.invoke({"context":context,"question":user})
        print("Bot: ",result)
        context += f"\nUser: {user}\nAI: {result}"
        
if __name__ == "__main__":
    convo()
