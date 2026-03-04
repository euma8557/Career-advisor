import streamlit as st
from google import genai
from dotenv import load_dotenv
import os

# Load .env
load_dotenv()

# Correct API key loading
api_key = os.getenv("GEMINI_API_KEY")

# Create Gemini client
client = genai.Client(api_key=api_key)

st.title("🎓 Career Advisor Chatbot")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

prompt = st.chat_input("Ask a career question...")

if prompt:

    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.write(prompt)

    try:
        with st.spinner("Thinking..."):

            response = client.models.generate_content(
                model="gemini-1.5-flash",
                contents=prompt
            )

            reply = response.text

    except Exception as e:
        reply = f"⚠ Error: {str(e)}"

    st.session_state.messages.append({"role": "assistant", "content": reply})

    with st.chat_message("assistant"):
        st.write(reply)