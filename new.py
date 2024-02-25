import openai
import json

openai.api_key = "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"
# Load and prepare the fine-tuning dataset
data = [
    {"prompt": "Hello", "completion": "Hi there! How can I help you?"},
    {"prompt": "What's the weather today?", "completion": "The weather today is sunny."},
    {"prompt": "Goodbye", "completion": "Goodbye! Have a great day!"}
]
with open("fine_tune_dataset.jsonl", "w") as f:
    for example in data:
        f.write(json.dumps(example) + "\n")

# Fine-tune the model
fine_tuned_model = openai.FineTune.create(
    engine="text-davinci-003",
    data="fine_tune_dataset.jsonl",
    n=1,
    epochs=1,
    validate=False
)

print(fine_tuned_model)