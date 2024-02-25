import openai
import json

openai.api_key = "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"

def chat_w_gpt(prompt):
  response = openai.ChatCompletion.create(
    model = "gpt-3.5-turbo",
    messages = [{"role": "user", "content": prompt}]
  )
  return response.choices[0].message.content.strip()


def fine_tune_gpt(data):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": data}],
        max_tokens=200,
        n=1,
        stop="\n"
    )
    return response.choices[0]["message"]["content"].strip()


if __name__ == "__main__":
    with open("physics.json", "r") as f:
        tech_conversations = json.load(f)
    
    # Prepare the data for fine-tuning
    fine_tune_data = ""
    for conversation in tech_conversations:
        fine_tune_data += f"User: {conversation['question']}\nAI: {conversation['answer']}\n"
    
    # Fine-tune the GPT-3.5 model on the data
    fine_tune_response = fine_tune_gpt(fine_tune_data)
    print(fine_tune_response)


    # while True:

    #   user_input = input("you: ")
    #   if user_input.lower() in ["quit", "exit", "bye"]:
    #     break
    #   response = chat_w_gpt(user_input)
    #   print("chat bot: ", response)
