import gradio as gr
import openai
from gtts import gTTS
import os
import speech_recognition as sr
import time


def open_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as infile:
        return infile.read()
openai.api_key = open_file('api_key.txt')


def chat_w_gpt(prompt):
    response = openai.ChatCompletion.create(
        model="ft:gpt-3.5-turbo-0613:personal::8wBiYAPJ",  # eng-ver.
        #model = "ft:gpt-3.5-turbo-0613:personal::8wtkKqNW", #vn ver.
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content.strip()

def text_to_speech(text):
    tts = gTTS(text=text, lang='en') # vi = vietnamese /// en = english
    return tts



# def chatbot_function(input_text):
#     bot_response = chat_w_gpt(input_text)
#     tts = text_to_speech(bot_response)
#     tts.save("output.mp3")
#     return bot_response, "output.mp3"



def chatbot_function(input_text):
    bot_response = chat_w_gpt(input_text)
    tts = text_to_speech(bot_response)
    relative_path = os.path.join('audio', 'output.mp3')
    tts.save(relative_path)
    return bot_response, relative_path, ""

iface = gr.Interface(
    fn=chatbot_function, 
    inputs=gr.Textbox(
        placeholder="Enter your question here...", 
        label="Ask me anything:", 
        lines=5
    ),
    outputs=[
        gr.Textbox(
            label="Response:", 
            lines=5
        ),
        gr.Audio(streaming="True")
    ],
    title="Chat with GPT-3.5 Turbo"
    
)

iface.launch()