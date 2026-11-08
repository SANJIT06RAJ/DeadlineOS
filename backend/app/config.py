import os
from pathlib import Path

# Backend directory
BASE_DIR = Path(__file__).resolve().parent.parent


# SQLite database configuration
DATABASE_PATH = (
    Path(
        os.getenv(
            "DATABASE_PATH",
            str(BASE_DIR / "deadlineos.db"),
        )
    )
    .expanduser()
    .resolve()
)


# Local Ollama configuration
OLLAMA_URL = os.getenv(
    "OLLAMA_URL",
    "http://localhost:11434/api/generate",
)

OLLAMA_MODEL = os.getenv(
    "OLLAMA_MODEL",
    "qwen2.5:3b",
)
