from ollama import chat
from datetime import datetime

def get_region_time(region):
    # Get the current time in the specified region
    now = datetime.now()
    return now.strftime("%Y-%m-%d %H:%M:%S")

region = input("Enter a region (e.g., 'New York', 'London', 'Tokyo'): ")
time_in_region = get_region_time(region)

response = chat(
    model='llama3.2',
    messages=[
        {
            'role': 'user',
            'content': f"What is the current time in {region}?"
        },
        {
            'role': 'system',
            'content': f"The current time in {region} is {time_in_region}."
        }
    ]
)

print(f"The current time in {region} is: {response['message']['content']}")