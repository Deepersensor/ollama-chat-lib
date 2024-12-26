import requests
import json
import sys
import os
import argparse

def load_config():
    with open(os.path.join(os.path.dirname(__file__), 'config.json'), 'r') as f:
        return json.load(f)

def generate_response(prompt, url, headers, model, stream):
    data = {
        "model": model,
        "prompt": prompt,
        "stream": stream
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))

    if response.status_code == 200:
        response_text = response.text
        data = json.loads(response_text)
        actual_response = data["response"]
        return actual_response
    else:
        return f"Error: {response.status_code}, {response.text}"

if __name__ == "__main__":
    config = load_config()

    parser = argparse.ArgumentParser(description="Ollama Chat Lib CLI")
    parser.add_argument("--url", type=str, default=config.get("url"), help="API URL")
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
        response = generate_response(prompt, args.url, headers, args.model, args.stream)
        print(f"Ollama: {response}")
