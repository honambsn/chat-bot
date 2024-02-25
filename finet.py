import openai 

def open_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as infile:
        return infile.read()

def save_file(filepath, content):
    with open(filepath, 'r', encoding='utf-8') as outfile:
        outfile.write(content)
        
api_key = open_file('api_key.txt')

openai.api_key = api_key

with open("D:/Ba Nam/nam 4 hoc ky 2/chatbot/demo/fix copy.jsonl","rb") as file:
    response = openai.File.create(
        file = file,
        purpose = 'fine-tune'
    )
file_id = response['id']
print(f"File uploaded with id: {file_id}")