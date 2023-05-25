import os
import subprocess
import uuid
from pathlib import Path
import openai
import json

# Set up OpenAI API
openai.api_key = "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"

def get_gpt_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.5,
    )
    return response.choices[0].text.strip()

def save_gpt_response(response):
    file_id = uuid.uuid4()
    file_name = f"gpt_response_id{file_id}.txt"
    with open(file_name, 'w') as output_file:
        output_file.write(response)
    return file_name

def main():
    script_request = input("Enter your script request: ")
    prompt = f"Write a Python script to {script_request}"
    gpt_response = get_gpt_response(prompt)
    response_file = save_gpt_response(gpt_response)
    subprocess.run(["python", "gpt_cleanup_bot.py", response_file])

if __name__ == "__main__":
    main()