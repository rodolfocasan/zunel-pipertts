# cencalang_pipertts/audio_utils.py
import io
import wave

import numpy as np





def _wav_bytes_to_pcm(wav_bytes: bytes) -> tuple[np.ndarray, int]:
    with wave.open(io.BytesIO(wav_bytes)) as wf:
        sr = wf.getframerate()
        n_frames = wf.getnframes()
        raw = wf.readframes(n_frames)
    samples = np.frombuffer(raw, dtype=np.int16).astype(np.float32)
    return samples, sr


def _pcm_to_wav_bytes(samples: np.ndarray, sample_rate: int) -> bytes:
    clipped = np.clip(samples, -32768, 32767).astype(np.int16)
    buf = io.BytesIO()
    with wave.open(buf, "wb") as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(sample_rate)
        wf.writeframes(clipped.tobytes())
    return buf.getvalue()


def _parse_rate(rate_str: str) -> float:
    rate_str = rate_str.strip()
    
    if not rate_str:
        return 1.0
    
    sign = 1.0 if rate_str[0] != "-" else -1.0
    pct = float(rate_str.lstrip("+-").rstrip("%"))
    return 1.0 + sign * pct / 100.0


def _parse_volume(vol_str: str) -> float:
    return _parse_rate(vol_str)


def _parse_pitch(pitch_str: str) -> float:
    pitch_str = pitch_str.strip()
    
    if not pitch_str:
        return 1.0
    
    sign = 1.0 if pitch_str[0] != "-" else -1.0
    val = float(pitch_str.lstrip("+-").rstrip("HzSst").strip())
    semitones = sign * val
    return 2.0 ** (semitones / 12.0)


def apply_pitch_shift(wav_bytes: bytes, pitch: str) -> bytes:
    pitch_factor = _parse_pitch(pitch)
    
    if pitch_factor == 1.0:
        return wav_bytes

    samples, sr = _wav_bytes_to_pcm(wav_bytes)

    try:
        from scipy.signal import resample
        shifted_len = int(len(samples) / pitch_factor)
        samples = resample(samples, max(shifted_len, 1))
        original_len = int(shifted_len * pitch_factor)
        samples = resample(samples, max(original_len, 1))
    except ImportError:
        pass
    return _pcm_to_wav_bytes(samples, sr)


def wav_to_mp3_bytes(wav_bytes: bytes) -> bytes:
    try:
        from pydub import AudioSegment
        buf = io.BytesIO(wav_bytes)
        seg = AudioSegment.from_wav(buf)
        out = io.BytesIO()
        seg.export(out, format="mp3", bitrate="128k")
        return out.getvalue()
    except Exception as exc:
        raise RuntimeError(
            "pydub/ffmpeg is required for MP3 output. "
            "Install with: pip install pydub  and ensure ffmpeg is available."
        ) from exc