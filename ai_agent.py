import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_community.tools.tavily_search import TavilySearchResults
from langgraph.prebuilt import create_react_agent
from tavily import TavilyClient
from langchain_core.messages import HumanMessage

load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")

if not GROQ_API_KEY:
    raise ValueError("GROQ_API_KEY is missing. Check your .env file.")
if not TAVILY_API_KEY:
    raise ValueError("TAVILY_API_KEY is missing. Check your .env file.")

tavily_client = TavilyClient(api_key=TAVILY_API_KEY)
groq_llm = ChatGroq(model="llama-3.3-70b-versatile", temperature=0.7)

system_prompt = "You are a smart and friendly AI chatbot. Answer the user's query directly and accurately."

def get_response_from_ai_agent(llm_id, query, allow_search, system_prompt, provider):
    if provider == "Groq":
        llm = ChatGroq(model=llm_id, temperature=0.7)
    else:
        raise ValueError("Unsupported provider. Only 'Groq' is supported currently.")
    
    tools = [TavilySearchResults(max_results=2)] if allow_search else []
    
    agent = create_react_agent(
        model=llm,
        tools=tools,
        state_modifier=system_prompt
    )

    input_state = {
        "messages": [HumanMessage(content=str(query))]
    }

    try:
        response = agent.invoke(input_state)
        messages = response.get("messages")
        if messages and len(messages) > 0:
            return messages[-1].content
        return str(response)
    except Exception as e:
        return f"Error: {str(e)}"

