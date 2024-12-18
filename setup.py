from setuptools import setup, find_packages

setup(
    name="ollama-chat-lib",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "requests",
    ],
    author="nathfavour",
    author_email="116535483+nathfavour@users.noreply.github.com",
    description="A Python library to interface with Ollama running locally",
    url="https://github.com/Deepersensor/ollama-chat-lib",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
