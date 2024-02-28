import gradio as gr
import openai
from gtts import gTTS
import os

openai.api_key = "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"

def chat_w_gpt(prompt):
    response = openai.ChatCompletion.create(
        #model="ft:gpt-3.5-turbo-0613:personal::8wBiYAPJ",  # eng-ver.
        model = "ft:gpt-3.5-turbo-0613:personal::8wtkKqNW", #vn ver.
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content.strip()

def text_to_speech(text):
    tts = gTTS(text=text, lang='en')
    return tts

def chatbot_function(input_text):
    bot_response = chat_w_gpt(input_text)
    tts = text_to_speech(bot_response)
    tts.save("output.mp3")
    return bot_response, "output.mp3"



iface = gr.Interface(fn=chatbot_function, 
                     inputs=gr.Textbox(placeholder="Enter your question here...", 
                                       label="Ask me anything:", 
                                       lines=5),
                     outputs=[gr.Textbox(label="Response:", 
                                         lines=5),
                              gr.HTML("<button onclick='playAudio()'>Play Audio</button><script>function playAudio() {var audio = new Audio('output.mp3'); audio.play();}</script>")],
                     title="Chat with GPT-3.5 Turbo")

iface.launch()