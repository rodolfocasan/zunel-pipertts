# cencalang_pipertts/config.py





MAX_TEXT_LENGTH = 5000
SAMPLE_RATE     = 22050
MODELS_DIR      = "models"

SPEED_RANGE  = (-50, 100)
VOLUME_RANGE = (-50, 100)
PITCH_RANGE  = (-20, 20)

HF_BASE_URL = "https://huggingface.co/rhasspy/piper-voices/resolve/main"


VOICE_CATALOG: dict[str, dict] = {
    "de-female-eva_k": {
        "language":      "de",
        "language_code": "de_DE",
        "gender":        "female",
        "speaker":       "eva_k",
        "quality":       "x_low",
        "description":   "German female voice (eva_k)",
        "syn_config": {
            "length_scale":  1.00,
            "noise_scale":   0.60,
            "noise_w_scale": 0.75,
        },
    },
    "de-male-pavoque": {
        "language":      "de",
        "language_code": "de_DE",
        "gender":        "male",
        "speaker":       "pavoque",
        "quality":       "low",
        "description":   "German male voice (pavoque)",
        "syn_config": {
            "length_scale":  1.00,
            "noise_scale":   0.60,
            "noise_w_scale": 0.75,
        },
    },
    "en-female-amy": {
        "language":      "en",
        "language_code": "en_US",
        "gender":        "female",
        "speaker":       "amy",
        "quality":       "medium",
        "description":   "US English female voice (amy)",
        "syn_config": {
            "length_scale":  1.00,
            "noise_scale":   0.667,
            "noise_w_scale": 0.80,
        },
    },
    "en-male-ryan": {
        "language":      "en",
        "language_code": "en_US",
        "gender":        "male",
        "speaker":       "ryan",
        "quality":       "medium",
        "description":   "US English male voice (ryan)",
        "syn_config": {
            "length_scale":  1.00,
            "noise_scale":   0.667,
            "noise_w_scale": 0.80,
        },
    },
    "es-latam-female-claude": {
        "language":      "es-latam",
        "language_code": "es_MX",
        "gender":        "female",
        "speaker":       "claude",
        "quality":       "high",
        "description":   "Mexican Spanish female voice (claude)",
        "syn_config": {
            "length_scale":  0.95,
            "noise_scale":   0.70,
            "noise_w_scale": 0.80,
        },
    },
    "es-latam-male-ald": {
        "language":      "es-latam",
        "language_code": "es_MX",
        "gender":        "male",
        "speaker":       "ald",
        "quality":       "medium",
        "description":   "Mexican Spanish male voice (ald)",
        "syn_config": {
            "length_scale":  0.95,
            "noise_scale":   0.70,
            "noise_w_scale": 0.80,
        },
    },
    "es-female-mls_10246": {
        "language":      "es",
        "language_code": "es_ES",
        "gender":        "female",
        "speaker":       "mls_10246",
        "quality":       "low",
        "description":   "Spain Spanish female voice (mls_10246)",
        "syn_config": {
            "length_scale":  1.00,
            "noise_scale":   0.667,
            "noise_w_scale": 0.80,
        },
    },
    "es-male-davefx": {
        "language":      "es",
        "language_code": "es_ES",
        "gender":        "male",
        "speaker":       "davefx",
        "quality":       "medium",
        "description":   "Spain Spanish male voice (davefx)",
        "syn_config": {
            "length_scale":  1.00,
            "noise_scale":   0.667,
            "noise_w_scale": 0.80,
        },
    },
    "fr-female-siwis": {
        "language":      "fr",
        "language_code": "fr_FR",
        "gender":        "female",
        "speaker":       "siwis",
        "quality":       "medium",
        "description":   "French female voice (siwis)",
        "syn_config": {
            "length_scale":  1.05,
            "noise_scale":   0.65,
            "noise_w_scale": 0.85,
        },
    },
    "fr-male-gilles": {
        "language":      "fr",
        "language_code": "fr_FR",
        "gender":        "male",
        "speaker":       "gilles",
        "quality":       "low",
        "description":   "French male voice (gilles)",
        "syn_config": {
            "length_scale":  1.05,
            "noise_scale":   0.65,
            "noise_w_scale": 0.85,
        },
    },
    "it-female-paola": {
        "language":      "it",
        "language_code": "it_IT",
        "gender":        "female",
        "speaker":       "paola",
        "quality":       "medium",
        "description":   "Italian female voice (paola)",
        "syn_config": {
            "length_scale":  0.95,
            "noise_scale":   0.72,
            "noise_w_scale": 0.82,
        },
    },
    "it-male-riccardo": {
        "language":      "it",
        "language_code": "it_IT",
        "gender":        "male",
        "speaker":       "riccardo",
        "quality":       "x_low",
        "description":   "Italian male voice (riccardo)",
        "syn_config": {
            "length_scale":  0.95,
            "noise_scale":   0.72,
            "noise_w_scale": 0.82,
        },
    },
    "pt-female-edresson": {
        "language":      "pt",
        "language_code": "pt_BR",
        "gender":        "female",
        "speaker":       "edresson",
        "quality":       "low",
        "description":   "Brazilian Portuguese female voice (edresson)",
        "syn_config": {
            "length_scale":  0.95,
            "noise_scale":   0.70,
            "noise_w_scale": 0.80,
        },
    },
    "pt-male-faber": {
        "language":      "pt",
        "language_code": "pt_BR",
        "gender":        "male",
        "speaker":       "faber",
        "quality":       "medium",
        "description":   "Brazilian Portuguese male voice (faber)",
        "syn_config": {
            "length_scale":  0.95,
            "noise_scale":   0.70,
            "noise_w_scale": 0.80,
        },
    },
    "ru-female-irina": {
        "language":      "ru",
        "language_code": "ru_RU",
        "gender":        "female",
        "speaker":       "irina",
        "quality":       "medium",
        "description":   "Russian female voice (irina)",
        "syn_config": {
            "length_scale":  1.05,
            "noise_scale":   0.65,
            "noise_w_scale": 0.80,
        },
    },
    "ru-male-dmitri": {
        "language":      "ru",
        "language_code": "ru_RU",
        "gender":        "male",
        "speaker":       "dmitri",
        "quality":       "medium",
        "description":   "Russian male voice (dmitri)",
        "syn_config": {
            "length_scale":  1.05,
            "noise_scale":   0.65,
            "noise_w_scale": 0.80,
        },
    },
}


DEFAULT_VOICE_CONFIG: dict[str, str] = {
    "de":       "de-male-pavoque",
    "en":       "en-male-ryan",
    "es-latam": "es-latam-male-ald",
    "es":       "es-male-davefx",
    "fr":       "fr-female-siwis",
    "it":       "it-female-paola",
    "pt":       "pt-male-faber",
    "ru":       "ru-female-irina",
}