from sarvamai import SarvamAI
from dotenv import load_dotenv
import os
import csv
import time


load_dotenv()
client = SarvamAI(
    api_subscription_key=os.getenv("SARVAM_API_KEY"),
)

result=[]
total_token=0
Successful=0
failed=0
prompt=0
#CSV FILE
with open("prompts.csv", "r", encoding="utf-8") as file:
    reader=csv.DictReader(file)

    for row in reader:
        prompt=row["prompt"]

        print("\nprocessing:",prompt)

        #start time
        start_time=time.time()
try:
    response = client.chat.completions(
    model="sarvam-105b",
    messages=[
        {"role": "user",
         "content":prompt
        }
    ],
)
    #end time
    end_time=time.time()

    #response time
    response_time=end_time-start_time

    print("Total time:",response_time)

    #response
    answer=response.choices[0].message.content

    # Estimated tokens
    token=len(answer.split())

    #Estimated API cost
    cost=token * 0.00001

    #total token
    total_token +=token
    Successful +=1

    #Display
    print("Response time:",response_time)
    print("Estimated tokens:",token)
    print("Estimated API cost:",cost)

    result.append([[
    prompt,
    answer,
    "Succes",
    token,
    cost
]])
except:
    failed +=1
    print("Succes: failed")
    print("error")

    result.append([
        prompt,
        " ",
        "Failed",
        0,
        0,
        0
    ])

    #Delay for rate limit
    time.sleep(2)
#Save Result
with open("results.csv", "w", encoding="utf-8") as file:

    writer = csv.writer(file)

    writer.writerow([
        "Prompt",
        "Response",
        "Status",
        "Response Time",
        "Estimated Tokens",
        "Estimated Cost"
    ])

    writer.writerows(result)

print("Total Prompts:", Successful + failed)
print("Successful Requests:", Successful)
print("Failed Requests:", failed)
print("Total Estimated Tokens:", response_time)
print("Total Estimated Cost:", response_time * 0.000001) 