# 🌟 Ollama Chat Lib 🌟

Welcome to **Ollama Chat Lib**! This is a powerful and easy-to-use Python library designed to interface with Ollama running locally. Whether you're building a chatbot, an AI assistant, or just experimenting with natural language processing, this library has got you covered.

## 🚀 Features

- **Seamless Integration**: Easily connect to your local Ollama instance.
- **Simple API**: Intuitive functions to generate responses.
- **Lightweight**: Minimal dependencies to keep your project lean.
- **Flexible**: Customize your prompts and models as needed.

## 📦 Installation

To install the library, simply run:

```bash
pip install .
```

## 🛠️ Usage

Here's a quick example to get you started:

```python
from ollama_chat_lib import generate_response

response = generate_response("Why is the sky blue?")
print(response)
```

## 🧪 Running Tests

To ensure everything is working correctly, you can run the included unit tests:

```bash
python -m unittest discover tests
```

## 🖥️ Interacting with the Models via cURL/Wget

Below are some example commands you can copy and modify to interact with your local Ollama instance directly:

### Using cURL

```bash
curl -X POST \
     -H "Content-Type: application/json" \
     -d '{
       "model": "qwen2.5-coder:0.5b",
       "messages": [{"role": "user", "content": "Hello, how are you?"}],
       "stream": false
     }' \
     http://localhost:11434/chat
```

### Using Wget

```bash
wget --method=POST \
     --header="Content-Type: application/json" \
     --body-data='{
       "model": "qwen2.5-coder:0.5b",
       "messages": [{"role": "user", "content": "Hello, how are you?"}],
       "stream": false
     }' \
     -O - \
     http://localhost:11434/chat
```

You can replace the model name, request body, or host URL as needed.

## 🤝 Contributing

We welcome contributions! If you'd like to contribute, please fork the repository and use a feature branch. Pull requests are warmly welcome.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🌟 Acknowledgements

- Thanks to the developers of [requests](https://docs.python-requests.org/en/latest/) and [setuptools](https://setuptools.pypa.io/en/latest/).
- Inspired by the need for robust local AI interactions.

## 📫 Contact

For any questions or suggestions, feel free to open an issue or contact the author at [116535483+nathfavour@users.noreply.github.com](mailto:116535483+nathfavour@users.noreply.github.com).

---

Happy coding! 🎉

