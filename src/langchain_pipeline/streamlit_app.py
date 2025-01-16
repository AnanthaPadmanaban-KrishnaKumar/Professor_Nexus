import streamlit as st
from chain import run_chain
import os
import sys
# Add src directory to PYTHONPATH
# Add src directory to PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

st.set_page_config(page_title="LangChain Chatbot", layout="wide")

# Initialize session state for chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Sidebar for settings
with st.sidebar:
    st.title("⚙️ Settings")
    mode = st.radio("Select Chatbot Mode:", ["Default", "Custom"], index=0)
    theme = st.radio("Choose Theme", ["Light", "Dark"], index=0)

    if theme == "Dark":
        st.markdown(
            "<style>body { background-color: #333; color: white; }</style>",
            unsafe_allow_html=True,
        )

    if mode == "Custom":
        model_id = st.selectbox("Choose Model", ["gpt-3.5", "gpt-4", "custom-model"])
        temperature = st.slider("Response Creativity (Temperature)", 0.0, 1.0, 0.7)
        max_tokens = st.number_input("Max Tokens", min_value=50, max_value=1000, value=200)
    else:
        model_id = "meta.llama3-2-1b-instruct-v1:0"
        temperature = 0.7
        max_tokens = 200

# Chatbot UI
st.title("🤖 LangChain Chatbot")
user_input = st.text_input("Type your message here:", key="user_input")

if st.button("Send"):
    if user_input.strip():
        # Add user input to session state
        st.session_state.chat_history.append(f"**You:** {user_input}")

        # Get chatbot response
        response = run_chain(user_input, model_id, temperature, max_tokens)
        st.session_state.chat_history.append(f"**Chatbot:** {response}")
    else:
        st.warning("Please enter a message before sending.")

# Display chat history
st.write("### Chat History")
for chat in st.session_state.chat_history:
    st.write(chat)
