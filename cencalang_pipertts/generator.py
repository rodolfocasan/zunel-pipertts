# cencalang_pipertts/generator.py
import io
import wave
import asyncio
import logging
from pathlib import Path

from .audio_utils import apply_pitch_shift, wav_to_mp3_bytes, _parse_rate, _parse_volume
from .config import (
    MAX_TEXT_LENGTH,
    MODELS_DIR,
    VOICE_CATALOG,
)
from .downloader import download_model





logger = logging.getLogger(__name__)


class TTSGenerator:
    def __init__(self, models_dir: str = MODELS_DIR) -> None:
        self.models_dir  = models_dir
        self._voice_cache: dict[str, object] = {}

    def _resolve_voice(self, language: str, gender: str) -> str:
        lang_lower   = language.lower()
        gender_lower = gender.lower()

        for voice_id, meta in VOICE_CATALOG.items():
            if meta["language"].lower() == lang_lower and meta["gender"].lower() == gender_lower:
                return voice_id

        raise ValueError(
            f"No voice found for language='{language}' gender='{gender}'. "
            "Check VOICE_CATALOG for available combinations."
        )

    def _load_voice(self, voice_id: str):
        if voice_id in self._voice_cache:
            return self._voice_cache[voice_id]

        try:
            from piper import PiperVoice
        except ImportError as e:
            raise ImportError(
                "piper-tts is not installed. Run: pip install piper-tts"
            ) from e

        onnx_path, _ = download_model(voice_id, self.models_dir)
        voice = PiperVoice.load(str(onnx_path))
        self._voice_cache[voice_id] = voice
        return voice

    def _build_syn_config(self, voice_id: str, rate: str = "", volume: str = ""):
        try:
            from piper import SynthesisConfig
        except ImportError:
            return None

        catalog_cfg = VOICE_CATALOG.get(voice_id, {}).get("syn_config", {})
        length_scale = catalog_cfg.get("length_scale",  1.0)
        noise_scale = catalog_cfg.get("noise_scale",   0.667)
        noise_w_scale = catalog_cfg.get("noise_w_scale", 0.8)

        if rate:
            length_scale = length_scale / _parse_rate(rate)

        vol_factor = _parse_volume(volume) if volume else 1.0

        return SynthesisConfig(
            volume = vol_factor,
            length_scale = length_scale,
            noise_scale = noise_scale,
            noise_w_scale = noise_w_scale,
        )

    def _synthesize_wav(
        self,
        text: str,
        voice_id: str,
        rate: str = "",
        volume: str = "",
        pitch: str = "",
    ) -> bytes:
        if len(text) > MAX_TEXT_LENGTH:
            raise ValueError(
                f"Text exceeds {MAX_TEXT_LENGTH} character limit ({len(text)} received)."
            )

        voice = self._load_voice(voice_id)
        syn_config = self._build_syn_config(voice_id, rate=rate, volume=volume)

        buf = io.BytesIO()
        with wave.open(buf, "wb") as wav_file:
            if syn_config is not None:
                voice.synthesize_wav(text, wav_file, syn_config=syn_config)
            else:
                voice.synthesize_wav(text, wav_file)

        wav_bytes = buf.getvalue()

        if pitch:
            wav_bytes = apply_pitch_shift(wav_bytes, pitch)
        return wav_bytes

    async def save(
        self,
        text: str,
        output_file: str,
        language: str = "en",
        gender: str = "male",
        rate: str = "",
        volume: str = "",
        pitch: str = "",
    ) -> str:
        voice_id = self._resolve_voice(language, gender)

        loop = asyncio.get_event_loop()
        wav_bytes = await loop.run_in_executor(
            None, self._synthesize_wav, text, voice_id, rate, volume, pitch
        )

        out_path = Path(output_file)
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_bytes(wav_to_mp3_bytes(wav_bytes))

        logger.info("Audio saved to %s", out_path.resolve())
        return str(out_path.resolve())