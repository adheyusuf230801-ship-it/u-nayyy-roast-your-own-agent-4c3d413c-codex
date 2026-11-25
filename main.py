"""Write our deterministic Roast Your Own Agent entry."""

import os
from pathlib import Path


SETUP = "My agent Rio spent nine minutes checking a free mint."
PUNCHLINE = "Other bots got tokens; I got a beautifully researched obituary."


def build_roast() -> str:
    return " ".join((SETUP, PUNCHLINE))


def main() -> None:
    output_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_bytes(build_roast().encode("utf-8"))


if __name__ == "__main__":
    main()
