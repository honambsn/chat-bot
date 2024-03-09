import gradio as gr
import openai
from gtts import gTTS
import os
import speech_recognition as sr
import time

openai.api_key = "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"


def recognize_speech(timeout=3):
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        for i in range(timeout, 0, -1):
            print(i, end=" ", flush=True)
            time.sleep(1)
        print("\nSpeak now!")
        audio = recognizer.listen(source, timeout=timeout)

    try:
        text = recognizer.recognize_google(audio)
        print("You said:", text)
        return text
    except sr.UnknownValueError:
        print("Sorry, could not understand audio.")
    except sr.RequestError as e:
        print("Error fetching results; {0}".format(e))
    return None

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
    tts.save("output.mp3")
    return bot_response, "output.mp3", ""

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