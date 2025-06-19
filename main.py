from pydantic import BaseModel
from fastapi import FastAPI
from typing import List
from ai_agent import get_response_from_ai_agent

class Request(BaseModel):
    model_name: str
    model_provider: str
    system_prompt: str
    allow_search: bool
    messages: List[str]

app = FastAPI(title="LangGraph ChatBot")

all_available_models = ["llama-3.3-70b-versatile", "gpt-4o-mini"]

@app.post('/chat')
def chat_endpoint(request: Request):
    if request.model_name not in all_available_models:
        return {"error": "Invalid model_name"}
    
    llm_id = request.model_name
    query = request.messages[-1] if request.messages else "" 
    system_prompt = request.system_prompt
    allow_search = request.allow_search
    provider = request.model_provider
    
    response = get_response_from_ai_agent(llm_id, query, allow_search, system_prompt, provider)
    print(query)
    return {"response": response}   