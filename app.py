import openai
import json

openai.api_key = "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"

def chat_w_gpt(prompt):
  response = openai.ChatCompletion.create(
    model = "ft:gpt-3.5-turbo-0613:personal::8wBiYAPJ", #eng-ver.
    #model = "ft:gpt-3.5-turbo-0613:personal::8wtkKqNW", vn ver.
    messages = [{"role": "user", "content": prompt}]
  )
  return response.choices[0].message.content.strip()


if __name__ == "__main__":

    while True:

      user_input = input("you: ")
      if user_input.lower() in ["quit", "exit", "bye"]:
        break
      response = chat_w_gpt(user_input)
      print("chat bot: ", response)
