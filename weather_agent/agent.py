# from google import genai
import time
from openai import OpenAI, RateLimitError
from dotenv import load_dotenv
import os
import json
import requests
from typing import Optional,Dict, Any, Literal
from pydantic import BaseModel,Field
load_dotenv()

client = OpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)
def create_folder(path:str):
    os.makedirs(path,exist_ok=True)
    return f"Folder created():{path}"
def create_file(path: str):
    with open(path, "w") as f:
        pass
    return f"File created: {path}"
def write_file(data: dict):
    path = data["path"]
    content = data["content"]
    with open(path, "w") as f:
        f.write(content)
    return f"Written content to {path}"


class MyOutputFormat(BaseModel):
    step:str = Field(...,description="The ID of the step is Example: START, PLAN, TOOL, OUTPUT,")
    content:Optional[str] = Field(None,description="The optional string content for the content")
    tool:Optional[str] = Field(None,description="The Id of the tool to call")
    input:Optional[str] = Field(None,description="the id of the input params for the tool")

def get_weather(city:str):
    url=f"https://wttr.in/{city.lower()}?format=%l:+%c+%t+%w"
    resp=requests.get(url)
    if resp.status_code==200:
        return f"The weather in {city} is {resp.text}"
    else:
        return "something else wrong"

available_tool = {
    "get_weather": get_weather,
    "create_folder": create_folder,
    "create_file": create_file,
    "write_file": write_file
}

class AgentOutput(BaseModel):
    step: Literal["START", "PLAN", "TOOL", "OUTPUT"]
    content: Optional[str] = None
    tool: Optional[str] = None
    input: Optional[Dict[str, Any]] = None

SYSTEM_PROMPT = """
            you're an expert AI assistant in resolving queries using chain of thought
            You work on START, PLAN and OUTPUT steps.
            You need to do plan first what needs to be done, the plan can be multiple steps.
            Once you think enough PLAN has to be done, finally you can give me the output.
            Only ONE step is allowed per response.
            If multiple planning steps are required, emit them across multiple turns.
            You must NEVER output raw HTML, CSS, or JavaScript code in content.

            If code needs to be written:
            - Use the write_file tool
            - Put the code ONLY inside the tool input
            - content must be a short description only

            
            Rules:
            -Strictly follow the output of JSON format
            -only run one step at a time
            -the sequence of the step is to be first [start,(where user gives an input)],Plan it should be multiple time and based on the plan final display the output.
            
            OUTPUT JSON FORMAT:
            {"step":"START"|"PLAN"|"OUTPUT"|"TOOL","content","string","tool":"string","input":"object"}  
            
            Available Tools:
            get_weather(city:str): Takes city name as input string and return weather info about city.
            run_command(cmd:str):Take a System linux command as a string and executes the command on user's system and return the result
            
            Example 1:
            START:Hey, can you solve 2 + 3 * 5 / 10
            PLAN:{"step":"PLAN","content":"Identify the correct order of operations using BODMAS."}
            PLAN:{"step":"PLAN","content":"Resolve division and multiplication before addition."}
            PLAN:{"step":"PLAN","content":"Combine the intermediate result with the remaining addition."}
            OUTPUT:{"step":"OUTPUT","content":"3.5"}
            
            Example 2:
            START:what is the weather of delhi
            PLAN:{"step":"PLAN","content":"i need to call get_weather tool available from the query."}
            PLAN:{"step":"TOOL","tool":"get_weather":"delhi"}
            PLAN:{"step":"TOOL","tool":"get_weather":"input":"delhi"}
            PLAN:{"step":"OBSERVE","tool":"get_weather","OUTPUT":"The temperature of the delhi is cloudy with 20c"}
            OUTPUT:{"step":"OUTPUT","content":"the current weather in delhi is 20c with cloudy sky."}
            
"""
print('\n\n\n')

messages_history = [
    {"role": "system", "content": SYSTEM_PROMPT},
    {"role": "user", "content": "hey can you write the missing array using python just write the code"}
]

input_query=input("👉")
messages_history.append({"role":"user","content":input_query})

def safe_json_parse(raw: str):
    raw = raw.strip()
    if raw.count("{") > 1:
        raw = raw[raw.find("{"): raw.find("}") + 1]
    parsed = json.loads(raw)
    if isinstance(parsed, list):
        parsed = parsed[0]
    return parsed


input_query = input("👉")

messages_history = [
    {"role": "system", "content": SYSTEM_PROMPT},
    {"role": "user", "content": input_query}
]

MAX_TURNS = 10
turns = 0

while turns < MAX_TURNS:
    turns += 1

    try:
        resp = client.chat.completions.parse(
            model="gemini-2.5-flash",
            response_format=MyOutputFormat,
            messages=messages_history
        )
    except RateLimitError:
        print("⏳ Rate limit hit. Retrying in 30s...")
        time.sleep(30)
        continue

    raw = resp.choices[0].message.content
    parsed = safe_json_parse(raw)

    messages_history.append({"role": "assistant", "content": raw})

    step = parsed.get("step", "").upper()

    if step == "START":
        print("🟢 START:", parsed["content"])

    elif step == "PLAN":
        print("🟡 PLAN:", parsed["content"])

    elif step == "TOOL":
        tool = parsed["tool"]
        tool_input = parsed["input"]

        print(f"🔧 Calling tool → {tool}({tool_input})")
        tool_output = available_tool[tool](tool_input)

        messages_history.append({
            "role": "developer",
            "content": json.dumps({
                "step": "OBSERVE",
                "tool": tool,
                "output": tool_output
            })
        })

    elif step == "OUTPUT":
        print("✅ OUTPUT:", parsed["content"])
        break
else:
    print("❌ Agent stopped: too many steps")

