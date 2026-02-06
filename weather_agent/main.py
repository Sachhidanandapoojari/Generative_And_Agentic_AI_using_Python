# from openai import OpenAI
# import os
# import requests
# from dotenv import load_dotenv
# load_dotenv()


# client = OpenAI(
#     api_key=os.getenv("GEMINI_API_KEY"),
#     base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
# )

# def get_weather(city:str):
#     url=f"https://wttr.in/{city.lower()}?format=%l:+%c+%t+%w"
#     response=requests.get(url)
#     if response.status_code==200:
#         return f"The weather in {city} is {response.text}"
#     return "Something else wrong"


# def main():
#     user_query=input("👉")
    
#     resp=client.chat.completions.create(
#         model="gemini-2.5-flash",
#         messages=[
#             {"role":"user","content":user_query}
#         ]
#     )
    
#     print(f"{resp.choices[0].message.content}")
# print(get_weather("gulbarga"))

from openai import OpenAI
import os
import requests
from dotenv import load_dotenv
load_dotenv()

client=OpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)
def get_weather(city:str):
    url=f"https://wttr.in/{city.lower()}?format=%l:+%c+%t+%w"
    resp=requests.get(url)
    if resp.status_code==200:
        return f"The weather in {city} is {resp.text}"
    else:
        return "something else wrong"
    
def main():
    user_query=input("👉")
    responses=client.chat.completions.create(
        model="gemini-2.5-flash",
        messages=[
            {"role":"user","content":user_query}
        ]
    )
    print(responses.choices[0].message.content)
print(get_weather("gulbarga"))





