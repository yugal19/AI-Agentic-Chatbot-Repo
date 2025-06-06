import streamlit as st

import requests

st.set_page_config(page_title="LangGraph Chatbot",layout="wide")
st.title("AI Agent ChatBot Using LangGraph")
st.write("Create and Interact with the AI agent")

system_prompt=st.text_area("Define your AI agent",height=70,placeholder="Type your prompt here")

Model_Names_Groq=["llama-3.3-70b-versatile","Not Another"]
Model_Names_OPEN_AI=["Free nHi haii "]

provider=st.radio("Select Provider:",("Groq","OpenAI"))

if provider=="Groq":
    selected_model=st.selectbox("select Groq Model",Model_Names_Groq)
else:
    selected_model=st.selectbox("select OpenAI Model",Model_Names_OPEN_AI)
    
    
allow_web_search=st.checkbox("Allow Web Search")

user_query=st.text_area("Enter your Query: ",height=150,placeholder="Ask Anything")

API_URL="http://127.0.0.1:8000/chat" 

if st.button("ASK AGENT"):
    if user_query.strip():  # removes the blank spacess
        
        payload={
            "model_name":selected_model,
            "model_provider": provider,
            "system_prompt": system_prompt,
            "allow_search": allow_web_search,
            "messages": [user_query]
        }
        response=requests.post(API_URL,json=payload)
        if response.status_code==200:
            response_data=response.json()
            if "error" in response_data:
                st.error(response_data["error"])
            else:
                st.subheader("Agent Response")
                st.markdown(f"**Final Response:**\n\n{response_data['response']}", unsafe_allow_html=True)

        