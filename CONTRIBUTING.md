# Contributing

Claude Code and Codex load the same skills. To add or update a skill, edit its
`SKILL.md` file in the [shared skills directory](plugins/astral/skills).

## Getting started

Clone the repository.

```bash
git clone https://github.com/astral-sh/claude-code-plugins
```

Add the checkout as a local marketplace and install the plugin.

| Step                      | Claude Code                                     | Codex CLI                                            |
| ------------------------- | ----------------------------------------------- | ---------------------------------------------------- |
| Add the local marketplace | `/plugin marketplace add ./claude-code-plugins` | `codex plugin marketplace add ./claude-code-plugins` |
| Install the plugin        | `/plugin install astral@astral-sh`              | `codex plugin add astral@astral-sh`                  |
