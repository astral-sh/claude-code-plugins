# Contributing

Claude Code and Codex load the same skills. To add or update a skill, edit its
`SKILL.md` file in the [shared skills directory](plugins/astral/skills).

## Getting started

Clone the repository.

```bash
git clone https://github.com/astral-sh/agent-plugins
```

From the directory containing the clone, add it as a local marketplace and
install the plugin.

### Codex

Run these commands in your shell.

```bash
codex plugin marketplace add ./agent-plugins
codex plugin add astral@astral-sh
```

### Claude Code

Run each command in a Claude Code session.

```text
/plugin marketplace add ./agent-plugins
```

```text
/plugin install astral@astral-sh
```

## Plugin manifests

Edit the marketplace catalog in `.agents/plugins/marketplace.json` and each
plugin's metadata in its root `plugin.json`. Codex reads these files directly.
Claude Code looks for the same files under `.claude-plugin/`. We ship regular
copies so the plugin also installs in Git checkouts with symlinks disabled.

After editing either manifest, regenerate the Claude Code copies.

```bash
uv run scripts/sync-manifests.py
```
