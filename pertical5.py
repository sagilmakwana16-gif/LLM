from sarvamai import SarvamAI
from dotenv import load_dotenv
import os
import json

load_dotenv()

client = SarvamAI(
    api_subscription_key=os.getenv('SARVAM_API_KEY'),
)


#History
message=[]
context_size=0

# Approx context limit
MAX_CONTEXT = 4096 
WARNING_LIMIT = int(MAX_CONTEXT * 0.50) 

#System
system=input("Enter system prompt:")
message.append({
    "role":"system",
    "content":system 
})


#message
while True:
    user_input=input("Enter your Prompt:")
    if user_input.lower()=="exit":
       break

    message.append({
        "role":"user",
        "content":user_input
    })
    response = client.chat.completions(
    model="sarvam-105b",
    messages=message
)
#AI Response save
    ai=response.choices[0].message.content
    print("AI Respons:",ai)

    message.append({
        "role":"assistant",
        "content":ai
})


 #Total messages exchanged
    total_message=len(message)//3
    print("Total Messages Exchanged:",total_message)

    print("Context size:",context_size)
# Total Token
    try:
       print("Total Token:", response.usage.total_tokens)
       context_size=response.usage.total_tokens

       
      if context_size >= WARNING_LIMIT and context_size<MAX_CONTEXT:
        print("⚠ WARNING: Conversation is approaching the model's context limit!")
       elif context_size>=MAX_CONTEXT:
          print("⚠ CONTEXT LIMIT HIT.")

    except:
     print("Total Token: Not Available")
     print("Context Size:", context_size) 
     


#Json File
with open("response.json","w") as file:
   json.dump(message,file,indent=3)
