"""File I/O helpers."""

import json
from dataclasses import asdict, is_dataclass
from pathlib import Path
from typing import Any


def save_json(data: Any, path: str | Path) -> None:
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    if is_dataclass(data):
        data = asdict(data)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, default=str)


def load_json(path: str | Path) -> Any:
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def read_text(path: str | Path) -> str:
    with open(path, encoding="utf-8") as f:
        return f.read()
