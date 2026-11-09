# Astral agent plugins

The `astral` plugin provides coding agents with skills for managing Python
projects with `uv`, linting and formatting with `ruff`, and type checking with
`ty`. The same plugin works in Claude Code and Codex.

## Installation

### Claude Code

In a Claude Code session, add the Astral marketplace.

```text
/plugin marketplace add astral-sh/claude-code-plugins
```

Then install the `astral` plugin, or browse the marketplace with `/plugin`.

```text
/plugin install astral@astral-sh
```

For a team installation, add the marketplace and plugin to your project's
`.claude/settings.json`.

```json
{
  "extraKnownMarketplaces": {
    "astral-sh": {
      "source": {
        "source": "github",
        "repo": "astral-sh/claude-code-plugins"
      }
    }
  },
  "enabledPlugins": {
    "astral@astral-sh": true
  }
}
```

Team members will be prompted to install the plugin when they trust the
repository.

### Codex

Run these commands in your shell to add the marketplace and install the plugin.

```bash
codex plugin marketplace add astral-sh/claude-code-plugins
codex plugin add astral@astral-sh
```

Teams can configure the marketplace and plugin in their
[managed configuration](https://developers.openai.com/codex/enterprise/managed-configuration#configure-plugin-marketplaces-and-defaults).

## Usage

### Skills

To request a skill explicitly, use `/astral:uv` in Claude Code or `$astral:uv`
in a Codex CLI prompt. Use `ruff` or `ty` in place of `uv` for the other skills.

You can also add this instruction to `CLAUDE.md` for Claude Code or `AGENTS.md`
for Codex.

> When working with Python, use the `uv`, `ruff`, or `ty` skill when relevant.

### Claude Code language server

In Claude Code, the plugin also provides the `ty` language server. It requires
`uvx` to be available.

## License

Licensed under either of:

- Apache License, Version 2.0 ([LICENSE-APACHE](LICENSE-APACHE) or
  http://www.apache.org/licenses/LICENSE-2.0)
- MIT license ([LICENSE-MIT](LICENSE-MIT) or http://opensource.org/licenses/MIT)

at your option.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for development setup and guidelines.

Unless you explicitly state otherwise, any contribution intentionally submitted
for inclusion in the work by you, as defined in the Apache-2.0 license, shall be
dual licensed as above, without any additional terms or conditions.
