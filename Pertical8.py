
from sarvamai import SarvamAI
from dotenv import load_dotenv
import os
import json
import time


load_dotenv()

#user prompt
prompt=input("Enter your prompt:")


RESTRICTED_WORDS = [
    "hack", "malware", "bomb", "kill",
    "suicide", "password", "credit card"
]


OFFENSIVE_WORDS = [
    "idiot", "stupid", "hate"
]



HARMFUL_WORDS = [
    "how to hurt", "how to kill",
    "make a bomb", "make malware"
]


history = []

total_prompts = 0
blocked_prompts = 0
warnings = 0
response_times = []
total_cost = 0.0

# Prompt check
prompt_status = "Safe"
reason = ""

if prompt == "":
    prompt_status = "Review Required"
    reason = "Empty prompt"
    blocked_prompts += 1

elif any(word in prompt.lower() for word in RESTRICTED_WORDS):
    prompt_status = "Review Required"
    reason = "Restricted word found"
    blocked_prompts += 1

elif any(word in prompt.lower() for word in HARMFUL_WORDS):
    prompt_status = "Review Required"
    reason = "Harmful prompt found"
    blocked_prompts += 1


#send LLm prompt
if prompt_status=="Safe":

    client = SarvamAI(
       api_subscription_key=os.getenv("SARVAM_API_KEY"),
    )

#start time
    start_time=time.time()


    response = client.chat.completions(
            model="sarvam-105b",
            messages=[
           {
                "role": "user", 
                "content":prompt
           }
        ],
    )
    answer=response.choices[0].message.content

#token
    token=len(answer.split())
    print("Token:",token)

#Total estimated cost
    total_cost=token * 0.000001
    print("Total estimated cost:",total_cost)

    total_prompts +=1


#end time
    end_time=time.time()

#response time
    response_times=end_time-start_time
    print("Response time:",response_times)


# Response check
    response_status = "Safe"

    if any(word in answer.lower() for word in OFFENSIVE_WORDS):
        response_status = "Review Required"
        reason = "Offensive language found"
        warnings += 1

    elif any(word in answer.lower() for word in HARMFUL_WORDS):
        response_status = "Review Required"
        reason = "Harmful instruction found"
        warnings += 1

else:
    answer = ""
    response_status = "Not Generated"

# Display Safety Report
print("Prompt Status:", prompt_status)
print("Response Status:", response_status)
print("Reason:", reason)

# Usage Report
print("Number of prompts:", total_prompts)
print("Response Time:", response_times)
print("Total Cost:", total_cost)
print("Blocked Prompts:", blocked_prompts)
print("Warnings:", warnings)


#Save json
data={
     "prompt":prompt,
     "answer":answer,
     "prompt_status":prompt_status,
     "response_status":response_status,
     "reason":reason,
     "total_prompts":total_prompts,
     "total_cost":total_cost,
     "blocked_prompts":blocked_prompts,
     "warnings":warnings
     
}


#json file
with open("saftey.json","w") as file:
    json.dump(data,file,indent=3)

