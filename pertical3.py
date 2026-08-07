from sarvamai import SarvamAI
import os
from dotenv import load_dotenv
import time

load_dotenv()

client = SarvamAI(
    api_subscription_key="sk_xnizbg83_dGjYvlfedeh1PJmMK77999nu"
)

#user Prompt
prompt=input("Enter your Prompt:")

# start time
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

# model name
Model_Name="sarvam-105b"

# Time End
end_time=time.time()

#Total time
total_time=start_time-end_time

#count
character=len(prompt)
word=len(prompt.split())

# Response Type
if word<=50:
    print("short")
elif word<=150:
    print("Medium")
else:
    print("long")
    

print(response.choices[0].message.content)
print(f"\nTotal Processing time:{total_time}")
print(f"\ncharacter lenth:{character}")
print(f"\nword lenth:{word}")
print(f"\nModel Name:{Model_Name}")