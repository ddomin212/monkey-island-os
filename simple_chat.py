import json
import os

import streamlit as st
from PIL import Image
from streamlit_javascript import st_javascript

from models import create_chatbot, generate_image, generate_narrator, prompt_chatbot
from prompts import GAME_PROMPT, IMAGE_PROMPT


def get_from_local_storage(k):
    v = st_javascript(f"JSON.parse(localStorage.getItem('{k}'));")
    return v


def set_to_local_storage(k, v):
    jdata = json.dumps(v)
    st_javascript(f"localStorage.setItem('{k}', JSON.stringify({jdata}));")


email = get_from_local_storage("email")
print(email)
if not email:
    with st.expander("Login to HuggingFace"):
        email = st.text_input("Email")
        passwd = st.text_input("Password", type="password")
        if st.button("Login"):
            game_chatbot = create_chatbot(email, passwd, 2, GAME_PROMPT, True)
            image_chatbot = create_chatbot(email, passwd, 0, IMAGE_PROMPT, True)
            set_to_local_storage("email", email)
else:
    game_chatbot = create_chatbot(email, "dummy", 2, GAME_PROMPT)
    image_chatbot = create_chatbot(email, "dummy", 0, IMAGE_PROMPT)

st.title("Monkey Island: Amsterdam")
st.subheader("Build with HuggingFace and Gradio, props to them :crown:")
st.markdown(
    "Also since its 100% free, you might encounter some weirdness, but chill man."
)
# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("Start the adventure"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    # Display assistant response in chat; message container
    with st.chat_message("assistant"):
        assistant_response = prompt_chatbot(game_chatbot, prompt)
        image_prompt = prompt_chatbot(image_chatbot, assistant_response)
        img_path = generate_image(image_prompt)
        audio_path = generate_narrator(assistant_response)

        image = Image.open(img_path)

        audio_file = open(audio_path, "rb")
        audio_bytes = audio_file.read()
        st.audio(audio_bytes, format="audio/mp3")

        st.image(image, caption="Generated Image", use_column_width=True)
        st.markdown(assistant_response)

    # Add assistant assistant_response to chat history
    st.session_state.messages.append(
        {"role": "assistant", "content": assistant_response}
    )
