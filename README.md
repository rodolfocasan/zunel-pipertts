# zunel-pipertts
Local, offline text-to-speech library powered by [Piper](https://github.com/rhasspy/piper) (VITS/ONNX). No cloud, no API key required. Outputs MP3.
---





## Installation
```bash
pip3 install git+https://github.com/rodolfocasan/zunel-pipertts
```

> **System dependency:** Piper requires `espeak-ng`. Install it before use.
>
> Debian/Ubuntu: `sudo apt install espeak-ng`
> macOS: `brew install espeak-ng`
> Windows: Download from the [espeak-ng releases page](https://github.com/espeak-ng/espeak-ng/releases).
---





## Quick start
```python
import asyncio
from cencalang_pipertts import TTSGenerator

async def main():
    gen = TTSGenerator(models_dir="models")

    await gen.save(
        "Hello, this is a local TTS test.",
        "output.mp3",
        language = "en",
        gender = "male",
    )

asyncio.run(main())
```


## TTSGenerator
```python
from cencalang_pipertts import TTSGenerator

gen = TTSGenerator(
    models_dir = "models",  # path where ONNX models are stored
)
```

`models_dir` controls where voice models are downloaded and cached. Defaults to `"models"` relative to the current working directory. Use an absolute path to keep models in a fixed location across different working directories.


### Save to MP3
```python
await gen.save(
    text = "The quick brown fox jumps over the lazy dog.",
    output_file = "speech.mp3",
    language = "en",
    gender = "male",
    rate = "+10%",
    volume = "+5%",
    pitch = "-2st",
)
```


## Downloading models
Models download automatically on first use. To download all voices at once upfront:
```python
from cencalang_pipertts import download_all_models

download_all_models(models_dir="models")
```


---
## Available voices

| Language | Code | Gender | Voice ID | Quality |
|---|---|---|---|---|
| German | `de` | M | `de-male-pavoque` | low |
| German | `de` | F | `de-female-eva_k` | x_low |
| English (US) | `en` | M | `en-male-ryan` | medium |
| English (US) | `en` | F | `en-female-amy` | medium |
| Spanish (MX) | `es-latam` | M | `es-latam-male-ald` | medium |
| Spanish (MX) | `es-latam` | F | `es-latam-female-claude` | high |
| Spanish (ES) | `es` | M | `es-male-davefx` | medium |
| Spanish (ES) | `es` | F | `es-female-mls_10246` | low |
| French | `fr` | M | `fr-male-gilles` | low |
| French | `fr` | F | `fr-female-siwis` | medium |
| Italian | `it` | M | `it-male-riccardo` | x_low |
| Italian | `it` | F | `it-female-paola` | medium |
| Portuguese (BR) | `pt` | M | `pt-male-faber` | medium |
| Portuguese (BR) | `pt` | F | `pt-female-edresson` | low |
| Russian | `ru` | M | `ru-male-dmitri` | medium |
| Russian | `ru` | F | `ru-female-irina` | medium |

Voice models are downloaded automatically from [Hugging Face](https://huggingface.co/rhasspy/piper-voices) on first use.