import os

import streamlit as st
from gradio_client import Client
from hugchat import hugchat
from hugchat.login import Login


def generate_image(prompt):
    client = Client(
        "https://openskyml-fast-sdxl-stable-diffusion-xl.hf.space/--replicas/545b5tw7n/"
    )
    result = client.predict(
        prompt,
        "text, blurry, 3d, cartoon, anime, (deformed eyes, nose, ears, nose), bad anatomy, ugly",  # str  in 'Negative Prompt' Textbox component
        25,  # int | float (numeric value between 1 and 30) in 'Sampling Steps' Slider component
        7,  # int | float (numeric value between 1 and 20) in 'CFG Scale' Slider component
        1024,  # int | float (numeric value between 1024 and 1024) in '↔️ Width' Slider component
        1024,  # int | float (numeric value between 1024 and 1024) in '↕️ Height' Slider component
        5,  # int | float  in 'Seed' Number component
        fn_index=0,
    )
    return result


def create_chatbot(email, passwd, index, prompt, first_time=False):
    if first_time:
        sign = Login(email, passwd)
        cookies = sign.login()

        cookie_path_dir = "./cookies_snapshot"
        sign.saveCookiesToDir(cookie_path_dir)

        return hugchat.ChatBot(
            cookies=cookies.get_dict(),
            default_llm=index,
            system_prompt=prompt,
        )
    else:
        return hugchat.ChatBot(
            cookie_path=f"./cookies_snapshot/{email}.json",
            default_llm=index,
            system_prompt=prompt,
        )


def prompt_chatbot(chatbot, text):
    query_result = chatbot.query(text)

    # print(query_result)

    info = chatbot.get_conversation_info()
    # print(info.id, info.title, info.model, info.system_prompt, info.history)

    return str(query_result)


def generate_narrator(prompt):
    client = Client("https://elevenlabs-tts.hf.space/")
    result = client.predict(prompt, "Rachel", fn_index=0)
    return result
