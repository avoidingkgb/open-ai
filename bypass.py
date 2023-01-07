import openai
import json
import os

os.system("title open ai chat bypass")

with open("config/config.json") as f:
    config = json.load(f)

openai.api_key = config["api_key"]

def chat(prompt):
    completions = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    message = completions.choices[0].text
    return message.strip()

while True:
    prompt = input("input your message : ")
    response = chat(prompt)
    print("Bot: ", response)