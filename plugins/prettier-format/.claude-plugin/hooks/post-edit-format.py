# /// script
# requires-python = ">=3.12"
# dependencies = []
# ///

"""Post-edit hook to auto-format files with prettier."""

import json
import os
import subprocess
import sys
from pathlib import Path


def main() -> None:
    input_data = json.load(sys.stdin)

    tool_name = input_data.get("tool_name")
    tool_input = input_data.get("tool_input", {})
    file_path = tool_input.get("file_path")

    if tool_name not in ("Write", "Edit", "MultiEdit"):
        return

    if not file_path:
        return

    path = Path(file_path)
    if path.suffix not in (".json5", ".yaml", ".yml", ".md"):
        return

    cwd = os.environ.get("CLAUDE_PROJECT_DIR", os.getcwd())

    try:
        subprocess.run(
            ["npx", "prettier", "--write", file_path],
            cwd=cwd,
            capture_output=True,
        )
    except FileNotFoundError:
        pass


if __name__ == "__main__":
    main()
