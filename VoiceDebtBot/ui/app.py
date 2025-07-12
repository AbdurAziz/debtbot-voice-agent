# Main app using Streamlit or Flask
import streamlit as st
import sys
import os
import json

sys.path.append("..")
from stt.whisper_stt import listen_and_transcribe
from llm.openai_llm import generate_agent_reply
from tts.tts_engine import speak_text

LOG_PATH = "../logs/conversation_log.json"

# Helper to log messages
def log_conversation(user_input, agent_reply):
    if os.path.exists(LOG_PATH):
        with open(LOG_PATH, "r") as f:
            history = json.load(f)
    else:
        history = []

    history.append({"user": user_input, "agent": agent_reply})
    with open(LOG_PATH, "w") as f:
        json.dump(history, f, indent=2)

# UI starts here
st.title("🎙️ Voice Agent Demo")
st.write("Click the button and speak. The agent will respond using GPT + TTS.")

if st.button("🔴 Start Voice Interaction"):
    user_input = listen_and_transcribe()

    if user_input.strip() == "":
        st.warning("No speech detected. Try again.")
    else:
        st.text(f"🧑 You said: {user_input}")
        agent_reply = generate_agent_reply(user_input)
        st.success(f"🤖 Agent: {agent_reply}")
        speak_text(agent_reply)
        log_conversation(user_input, agent_reply)

# Show past conversations
st.subheader("📜 Conversation History")
if os.path.exists(LOG_PATH):
    with open(LOG_PATH, "r") as f:
        logs = json.load(f)
        for entry in reversed(logs[-5:]):
            st.write(f"🧑 {entry['user']}")
            st.write(f"🤖 {entry['agent']}")
            st.markdown("---")
