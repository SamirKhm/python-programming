import openai
from openai import OpenAi
# key - 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

key="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"



client = OpenAI(
    api_key=key,
)
messages=[]

def completion(message):
    global messages
    completion = client.chat.completions.create(
    
    messages={
        
            "role": "assitant",
            "content":chat_completion.choices.message.content,
        }
    messages.append(message)
    

print(chat_completion)
if __name__=="__main__":
    user_question=input("Hi , I am Jarvis , How may i help you")
    completion(user_question)