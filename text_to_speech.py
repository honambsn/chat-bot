import openai
from gtts import gTTS
import os

# Set up your OpenAI API key
openai.api_key = "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"

def chat_with_bot(prompt):
  response = openai.ChatCompletion.create(
        #model="ft:gpt-3.5-turbo-0613:personal::8wBiYAPJ", #eng
        model="ft:gpt-3.5-turbo-0613:personal::8wtkKqNW", #vn
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )
  return response.choices[0].message.content.strip()

def text_to_speech(text, filename="output.mp3"):
    tts = gTTS(text=text, lang='en')
    tts.save(filename)
    return filename

if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit", "bye"]:
            print("Exiting...")
            break

        bot_response = chat_with_bot(user_input)
        print("Bot:", bot_response)

        speech_file = text_to_speech(bot_response)
        os.system("start " + speech_file)  # Open the speech file (works on Windows)

        # For other operating systems, you might need different commands to play the audio.