# cencalang_pipertts/downloader.py
import logging
from pathlib import Path

import requests

from .config import HF_BASE_URL, MODELS_DIR, VOICE_CATALOG





logger = logging.getLogger(__name__)


def _build_hf_paths(voice_id: str) -> tuple[str, str]:
    meta = VOICE_CATALOG[voice_id]
    lc = meta["language_code"]
    spk = meta["speaker"]
    q = meta["quality"]
    lang_fam = lc.split("_")[0]
    base_name = f"{lc}-{spk}-{q}"
    remote = f"{HF_BASE_URL}/{lang_fam}/{lc}/{spk}/{q}"
    return f"{remote}/{base_name}.onnx", f"{remote}/{base_name}.onnx.json"


def _local_paths(voice_id: str, models_dir: str = MODELS_DIR) -> tuple[Path, Path]:
    meta = VOICE_CATALOG[voice_id]
    lc = meta["language_code"]
    spk = meta["speaker"]
    q = meta["quality"]
    base_name = f"{lc}-{spk}-{q}"
    folder = Path(models_dir) / lc
    folder.mkdir(parents=True, exist_ok=True)
    return folder / f"{base_name}.onnx", folder / f"{base_name}.onnx.json"


def is_model_cached(voice_id: str, models_dir: str = MODELS_DIR) -> bool:
    onnx_path, json_path = _local_paths(voice_id, models_dir)
    return onnx_path.exists() and json_path.exists()


def _download_file(url: str, dest: Path) -> None:
    logger.info("Downloading %s -> %s", url, dest)
    try:
        with requests.get(url, stream=True, timeout=60) as response:
            response.raise_for_status()
            total = int(response.headers.get("content-length", 0))
            downloaded = 0
            with open(dest, "wb") as f:
                for chunk in response.iter_content(chunk_size=8192):
                    if chunk:
                        f.write(chunk)
                        downloaded += len(chunk)
                        if total > 0:
                            pct = min(100, downloaded * 100 // total)
                            print(f"\r  {dest.name}: {pct:3d}%", end="", flush=True)
        print()
    except Exception as exc:
        if dest.exists():
            dest.unlink()
        raise RuntimeError(f"Error downloading {url}: {exc}") from exc


def download_model(voice_id: str, models_dir: str = MODELS_DIR) -> tuple[Path, Path]:
    if voice_id not in VOICE_CATALOG:
        raise ValueError(f"Unknown voice: '{voice_id}'.")

    onnx_path, json_path = _local_paths(voice_id, models_dir)

    if not onnx_path.exists() or not json_path.exists():
        onnx_url, json_url = _build_hf_paths(voice_id)
        print(f"[cencalang_pipertts] Downloading model '{voice_id}'...")

        if not onnx_path.exists():
            _download_file(onnx_url, onnx_path)

        if not json_path.exists():
            _download_file(json_url, json_path)

        print(f"[cencalang_pipertts] Model '{voice_id}' ready.")
    else:
        logger.debug("Model '%s' already cached: %s", voice_id, onnx_path)
    return onnx_path, json_path


def download_all_models(models_dir: str = MODELS_DIR) -> None:
    total  = len(VOICE_CATALOG)
    done   = 0
    failed = 0

    for voice_id in VOICE_CATALOG:
        try:
            download_model(voice_id, models_dir)
            done += 1
        except Exception as exc:
            failed += 1
            logger.error("Failed to download '%s': %s", voice_id, exc)
    print(f"[cencalang_pipertts] Done: {done}/{total} | Failed: {failed}")