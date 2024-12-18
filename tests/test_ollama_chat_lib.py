import unittest
from ollama_chat_lib import generate_response

class TestOllamaChatLib(unittest.TestCase):
    def test_generate_response(self):
        response = generate_response("Why is the sky blue?")
        self.assertIsInstance(response, str)

if __name__ == "__main__":
    unittest.main()
