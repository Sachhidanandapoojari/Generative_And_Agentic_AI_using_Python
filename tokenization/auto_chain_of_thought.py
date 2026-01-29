# from google import genai
import time
from openai import OpenAI, RateLimitError
from dotenv import load_dotenv
import os
import json
load_dotenv()

client = OpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

SYSTEM_PROMPT = """
            you're an expert AI assistant in resolving queries using chain of thought
            You work on START, PLAN and OUTPUT steps.
            You need to do plan first what needs to be done, the plan can be multiple steps.
            Once you think enough PLAN has to be done, finally you can give me the output.
            
            Rules:
            -Strictly follow the output of JSON format
            -only run one step at a time
            -the sequence of the step is to be first [start,(where user gives an input)],Plan it should be multiple time and based on the plan final display the output.
            
            OUTPUT JSON FORMAT:
            {"step":"START"|"PLAN"|"OUTPUT","content","string"}  
            
            Example:
            START:Hey, can you solve 2 + 3 * 5 / 10
            PLAN:{"step":"PLAN","content":"Identify the correct order of operations using BODMAS."}
            PLAN:{"step":"PLAN","content":"Resolve division and multiplication before addition."}
            PLAN:{"step":"PLAN","content":"Combine the intermediate result with the remaining addition."}
            OUTPUT:{"step":"OUTPUT","content":"3.5"}            
"""
print('\n\n\n')

messages_history = [
    {"role": "system", "content": SYSTEM_PROMPT},
    {"role": "user", "content": "hey can you write the missing array using python just write the code"}
]

input_query=input("👉")
messages_history.append({"role":"user","content":input_query})


while True:
        resp=client.chat.completions.create(
            model="gemini-2.5-flash", 
            response_format={"type":"json_object"},
            messages=messages_history
        )

        raw_data=(resp.choices[0].message.content.strip())
        messages_history.append({"role":"assistant","content":raw_data})
        parsed_res=json.loads(raw_data)
        
        step = parsed_res.get("step", "").strip().upper()
        content = parsed_res.get("content", "")
        
        if step == "START":
            print("🟢 START:", content)
            continue
        elif step == "PLAN":
            print("🟡 PLAN:", content)
            continue
        elif step == "OUTPUT":
            print("✅ OUTPUT:", content)
            break