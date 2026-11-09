"""Copy the shared manifests to the paths Claude Code discovers."""

from pathlib import Path
from shutil import copyfile


def copy_for_claude(source: Path, directory: Path) -> None:
    destination = directory / ".claude-plugin" / source.name
    destination.parent.mkdir(exist_ok=True)
    copyfile(source, destination)


root = Path(__file__).resolve().parents[1]
copy_for_claude(root / ".agents/plugins/marketplace.json", root)
for manifest in (root / "plugins").glob("*/plugin.json"):
    copy_for_claude(manifest, manifest.parent)
