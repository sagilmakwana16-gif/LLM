from sarvamai import SarvamAI
import os
from dotenv import load_dotenv
import time
import json

load_dotenv()

client = SarvamAI(
    api_subscription_key=os.getenv('SARVAM_API_KEY')
)
#user Prompt
prompt=input("Enter your Prompt:")
Model_Name=input("Enter Your Model:")  # Model Name:sarvam-105b
temperature=input("Enter Temperature:")
top_p=input("Enter Top-p:")
maximum_tokens=int(input("Enter Maximum Tokens:"))
stop_Sequence=input("Enter Stop Sequence:")

start_time=time.time()

response = client.chat.completions(
    model=Model_Name,
    messages=[
        {
            "role": "user", 
            "content":prompt,
            
        }
    ],
temperature=float(temperature),
top_p=float(top_p),
max_tokens=maximum_tokens,
stop=stop_Sequence if stop_Sequence else None,
reasoning_effort=None

)
#Generated Response
answer=response.choices[0].message.content

end_time=time.time()

#Response Time
total_time=end_time-start_time

print("response time =",answer)
#Model Name
print(f"Model Name:{Model_Name}")
print(f"Response Time:{total_time}")
#finish_reason
print("finish_reason:",response.choices[0].finish_reason)
print(response.choices[0].message.content)



#data for json
data={
    "prompt":prompt,
    "Model_Name":Model_Name,
    "temperature":temperature,
    "top_p":top_p,
    "maximum_tokens":maximum_tokens,
    "stop_Sequence":stop_Sequence,
    "total_time":total_time,
    "answer":answer,
    "finish_reason":response.choices[0].finish_reason
}

with open("response.choices[0].json","w") as file:
    json.dump(data,file,indent=4)