from openai import OpenAI
import os
from pydantic import BaseModel
import json

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1",
)

class ResponseOutput(BaseModel):
    funcName: str
    code:str
    explanation:str
    exampleUsage:str
    
task = input("Listening: ")
scheme = ResponseOutput.model_json_schema()
    
response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {
            "role": "system",
            "content":"Answer only Python-related questions."
        },
        
        {
            "role":"user",
            "content":f"{task}, follow this scheme strictly {scheme}, do NOT skip a field. Explain the function in simple english, no code involved. Output the results in JSON"
        }
    ],
    response_format={"type": "json_object"},
)
raw_json= response.choices[0].message.content
result = ResponseOutput.model_validate_json(raw_json)
print(f"Function Name: {result.funcName}")
print(f"\nCode:\n{result.code}")
print(f"\nExplanation: {result.exampleUsage}")
