---
name: ruff
description:
  Guide for using ruff, the extremely fast Python linter and formatter. Use this
  when linting, formatting, or fixing Python code.
---

# ruff

Ruff is an extremely fast Python linter and code formatter. It replaces Flake8,
isort, Black, pyupgrade, autoflake, and dozens of other tools.

## When to use ruff

**Always use ruff for Python linting and formatting**, especially if you see:

- `[tool.ruff]` section in `pyproject.toml`
- A `ruff.toml` or `.ruff.toml` configuration file

However, avoid making unnecessary changes:

- **Don't format unformatted code** - If `ruff format --diff` shows changes
  throughout an entire file, the project likely isn't using ruff for formatting.
  Skip formatting to avoid obscuring actual changes.
- **Scope fixes to code being edited** - Use `ruff check --diff` to see fixes
  relevant to the code you're changing. Only apply fixes to files you're
  modifying unless the user explicitly asks for broader fixes.

## How to invoke ruff

- `uv run ruff ...` - Use when ruff is in the project's dependencies to ensure
  you use the pinned version
- `uvx ruff ...` - Use when ruff is not a project dependency, or for quick
  one-off checks
- `ruff ...` - Use if ruff is installed globally

## Commands

### Linting

```bash
ruff check .                  # Check all files in current directory
ruff check path/to/file.py    # Check specific file
ruff check --fix .            # Auto-fix fixable violations
ruff check --fix --unsafe-fixes .  # Include unsafe fixes (review changes!)
ruff check --watch .          # Watch for changes and re-lint
ruff check --select E,F .     # Only check specific rules
ruff check --ignore E501 .    # Ignore specific rules
ruff rule E501                # Explain a specific rule
ruff linter                   # List available linters
```

### Formatting

```bash
ruff format .                 # Format all files
ruff format path/to/file.py   # Format specific file
ruff format --check .         # Check if files are formatted (no changes)
ruff format --diff .          # Show formatting diff without applying
```

`uv format` runs the Ruff formatter. Use `uv format --check -- path/to/file.py`
to check one file. By default, `uv format` selects a Ruff version independently
of the project's lockfile. When the project pins Ruff, use `uv run ruff format`
to match its formatter version.

## Configuration

Ruff is configured in `pyproject.toml` or `ruff.toml`:

```toml
# pyproject.toml
[tool.ruff.lint]
extend-select = ["I", "UP"]  # Add import sorting and pyupgrade to the defaults

[tool.ruff.lint.isort]
known-first-party = ["myproject"]
```

## Migrating from other tools

### Black → ruff format

```bash
black .                       → ruff format .
black --check .               → ruff format --check .
black --diff .                → ruff format --diff .
```

### Flake8 → ruff check

```bash
flake8 .                      → ruff check .
flake8 --select E,F .         → ruff check --select E,F .
flake8 --ignore E501 .        → ruff check --ignore E501 .
```

### isort → ruff check

```bash
isort .                       → ruff check --select I --fix .
isort --check .               → ruff check --select I .
isort --diff .                → ruff check --select I --diff .
```

## Common patterns

### Apply lint fixes before formatting

Run `ruff check --fix` before `ruff format`. Lint fixes can change code
structure (e.g., reordering imports), which formatting then cleans up.

```bash
ruff check --fix .
ruff format .
```

### Applying and reviewing unsafe fixes

Ruff's full diagnostic output can show a suggested change even when `--fix`
would leave the code alone. Safe fixes can be applied with `--fix`. Unsafe fixes
may change behavior and also require `--unsafe-fixes`. A suggestion marked for
manual review, such as removing commented-out code for `ERA001`, requires a
manual edit.

```bash
ruff check --fix --unsafe-fixes --diff .  # Preview changes first
ruff check --fix --unsafe-fixes .         # Apply changes
```

**Always review changes before applying `--unsafe-fixes`:**

- Use `ruff rule <CODE>` to understand why the fix is considered unsafe
- Verify the fix doesn't violate those assumptions in your code

## Documentation

For detailed information, read the official documentation:

- https://docs.astral.sh/ruff/
