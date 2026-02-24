# setup.py
from setuptools import setup, find_packages


with open("README.md", encoding="utf-8") as f:
    long_description = f.read()


setup(
    name = "zunel-pipertts",
    version = "1.0.0",
    description = "Local TTS library powered by PiperTTS (VITS/ONNX): offline MP3 synthesis.",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    author = "rodolfocasan",
    url = "https://github.com/rodolfocasan/zunel-pipertts",
    python_requires = ">=3.10",
    packages = find_packages(),
    install_requires = [
        "piper-tts>=1.2.0",
        "numpy>=1.24.0",
        "scipy>=1.10.0",
        "pydub>=0.25.0",
        "requests>=2.28.0",
    ],
    classifiers = [
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Operating System :: OS Independent",
        "Topic :: Multimedia :: Sound/Audio :: Speech",
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
    ],
)