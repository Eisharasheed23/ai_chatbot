import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load API key from .env file
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Initialize the Gemini model
# Initialize the Gemini model with the valid model name
model = genai.GenerativeModel("models/gemini-1.5-flash")




# Streamlit app setup
st.set_page_config(page_title="💬 AI Chatbot")
st.title("🤖 Talk to AI (Gemini)")

if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    st.chat_message(message["role"]).write(message["content"])

# User input
user_input = st.chat_input("Type your message here...")



if user_input:
    st.chat_message("user").write(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Custom reply if user asks who created the chatbot
    if "who created you" in user_input.lower():
        reply = "I was created by Eisha Rasheed! 🌟"
    else:
        try:
            response = model.generate_content(user_input)
            reply = response.text
        except Exception as e:
            reply = f"Oops! Something went wrong: {e}"

    st.chat_message("assistant").write(reply)
    st.session_state.messages.append({"role": "assistant", "content": reply})
