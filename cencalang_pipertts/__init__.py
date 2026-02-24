# cencalang_pipertts/__init__.py
import logging

from .config import (
    DEFAULT_VOICE_CONFIG,
    MAX_TEXT_LENGTH,
    MODELS_DIR,
    PITCH_RANGE,
    SAMPLE_RATE,
    SPEED_RANGE,
    VOICE_CATALOG,
    VOLUME_RANGE,
)
from .downloader import download_all_models
from .generator import TTSGenerator





class _MissingPhonemeFilter(logging.Filter):
    def filter(self, record):
        return "Missing phoneme from id map" not in record.getMessage()

logging.getLogger("piper.voice").addFilter(_MissingPhonemeFilter())


__version__ = "1.0.0"
__all__ = [
    "TTSGenerator",
    "download_all_models",
    "DEFAULT_VOICE_CONFIG",
    "MAX_TEXT_LENGTH",
    "MODELS_DIR",
    "SAMPLE_RATE",
    "SPEED_RANGE",
    "VOLUME_RANGE",
    "PITCH_RANGE",
    "VOICE_CATALOG",
]