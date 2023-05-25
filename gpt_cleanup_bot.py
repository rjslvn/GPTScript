import openai
import sys
import os
from pathlib import Path

openai.api_key = "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"

def get_gpt_cleanup_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=200,
        n=1,
        stop=None,
        temperature=0.5,
    )
    return response.choices[0].text.strip()

def save_cleaned_code(response):
    folder_path = Path("ai_dev")
    folder_path.mkdir(parents=True, exist_ok=True)
    file_name = "codename.py"
    with open(folder_path / file_name, 'w') as output_file:
        output_file.write(response)

def main():
    if len(sys.argv) != 2:
        print("Usage: python gpt_cleanup_bot.py <response_file>")
        return
    
    response_file = sys.argv[1]
    
    with open(response_file, 'r') as file:
        gpt_response = file.read()
    
    prompt = f"I'm going to paste an output of text to you that has the code to a python program. Can you return (and this is extremely important) that to me as ONLY the code itself formatted with the correct whitespace, etc that i can copy it exactly and run it right after? The response is: {gpt_response}"
    cleaned_code = get_gpt_cleanup_response(prompt)
    save_cleaned_code(cleaned_code)
    os.remove(response_file)

if __name__ == "__main__":
    main()
