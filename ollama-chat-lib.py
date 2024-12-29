import sys
import os
import argparse
import json
from ollama import Client

def load_config():
    with open(os.path.join(os.path.dirname(__file__), 'config.json'), 'r') as f:
        return json.load(f)

def generate_response(prompt, host, headers, model, stream):
    client = Client(host=host, headers=headers)
    if stream:
        text = ""
        for chunk in client.chat(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            stream=True
        ):
            text += chunk["message"]["content"]
        return text
    else:
        result = client.chat(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            stream=False
        )
        return result.message.content

if __name__ == "__main__":
    config = load_config()

    parser = argparse.ArgumentParser(description="Ollama Chat Lib CLI")
    parser.add_argument("--host", type=str, default=config.get("host"), help="Ollama host")
    parser.add_argument("--model", type=str, default=config.get("model"), help="Model name")
    parser.add_argument("--stream", type=bool, default=config.get("stream"), help="Stream response")
    args = parser.parse_args()

    headers = config.get("headers")

    print("Ollama Chat Lib CLI. Type your prompt and press Enter. Type 'exit' to quit.")
    while True:
        prompt = input("You: ")
        if prompt.lower() == 'exit':
            print("Exiting...")
            break
        response = generate_response(prompt, args.host, headers, args.model, args.stream)
        print(f"Ollama: {response}")
