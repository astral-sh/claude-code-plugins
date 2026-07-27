# Astral plugins for Claude Code

## Installation

### Add the marketplace

Add the Astral marketplace to Claude Code:

```bash
/plugin marketplace add astral-sh/claude-code-plugins
```

### Install the plugins

After adding the marketplace:

```bash
# Skills for uv, ruff, and ty
/plugin install astral@astral-sh

# Optional ty language server
/plugin install ty-lsp@astral-sh
```

Or browse and install interactively:

```bash
/plugin
```

### Team installation

For team-wide plugin usage, add to your project's `.claude/settings.json`:

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
    "astral@astral-sh": true,
    "ty-lsp@astral-sh": true
  }
}
```

Team members will be prompted to install the plugin when they trust the
repository. Omit `ty-lsp@astral-sh` when the project uses a different language
server.

### Migrating from the combined plugin

The `astral` plugin now contains only the uv, ruff, and ty skills. To keep the
ty language server after updating the marketplace, install the separate plugin:

```bash
/plugin install ty-lsp@astral-sh
```

If you use another Python language server, no replacement is needed.

## Usage

### Skills

The `astral` plugin provides skills for Astral tools.

Invoke skills with `/astral:<skill>`, e.g., `/astral:uv`.

Claude sometimes needs to be prompted to use skills. We recommend adding this
instruction to your `CLAUDE.md`:

> When working with Python, invoke the relevant `/astral:<skill>` for `uv`,
> `ty`, and `ruff` to ensure best practices are followed.

### LSP

The optional `ty-lsp` plugin provides the ty LSP for Python files (`.py` and
`.pyi`). It requires `uvx` to be available.

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
