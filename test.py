import openai
import gradio as gr

openai.api_key = "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"

def chat_w_gpt(prompt):
    response = openai.ChatCompletion.create(
        model="ft:gpt-3.5-turbo-0613:personal::8wBiYAPJ",  # eng-ver.
        # model = "ft:gpt-3.5-turbo-0613:personal::8wtkKqNW", vn ver.
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content.strip()

def chatbot_function(input_text):
    return chat_w_gpt(input_text)




iface = gr.Interface(fn=chatbot_function, 
                     inputs=gr.Textbox(placeholder="Enter your question here...", 
                                       label="Ask me anything:", 
                                       lines=5),
                     outputs=gr.Textbox(label="Response:", 
                                        lines=5),
                     title="Chat with GPT-3.5 Turbo")

iface.launch()