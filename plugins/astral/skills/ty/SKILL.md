---
name: ty
description:
  Type check Python and investigate diagnostics with ty. Use when a project
  configures or runs ty, or when the user asks to set up or migrate to ty.
---

# ty

ty is an extremely fast Python type checker and language server. It replaces
mypy, Pyright, and other type checkers.

## When to use ty

Use ty when requested or when the project already uses it. Look for `[tool.ty]`
in `pyproject.toml`, a `ty.toml` file, or a `ty check` invocation in CI.

## How to invoke ty

- `uv run ty ...` - Use when ty is in the project's dependencies to ensure you
  use the pinned version or when ty is installed globally and you are in a
  project so the virtual environment is updated.
- `uvx ty ...` - Use when ty is not a project dependency, or for quick one-off
  checks

## Commands

### Type checking

```bash
ty check                      # Check all files in current directory
ty check path/to/file.py      # Check specific file
ty check src/                 # Check specific directory
```

### Rule configuration

```bash
ty check --error possibly-unresolved-reference   # Treat as error
ty check --warn division-by-zero                 # Treat as warning
ty check --ignore unresolved-import              # Disable rule
```

### Python version targeting

```bash
ty check --python-version 3.12     # Check against Python 3.12
ty check --python-platform linux   # Target Linux platform
```

## Configuration

ty is configured in `pyproject.toml` or `ty.toml`:

```toml
# pyproject.toml
[tool.ty.environment]
python-version = "3.12"

[tool.ty.rules]
possibly-unresolved-reference = "warn"
division-by-zero = "error"

[tool.ty.src]
include = ["src/**/*.py"]
exclude = ["**/migrations/**"]

[tool.ty.terminal]
output-format = "full"
error-on-warning = false
```

### Per-file overrides

Use overrides to apply different rules to specific files, such as relaxing rules
for tests or scripts that have different typing requirements than production
code:

```toml
[[tool.ty.overrides]]
include = ["tests/**", "**/test_*.py"]

[tool.ty.overrides.rules]
possibly-unresolved-reference = "warn"
```

## Language server

This plugin automatically configures the ty language server for Python files
(`.py` and `.pyi`).

## Migrating from other tools

### mypy → ty

```bash
mypy .                        → ty check
mypy --strict .               → ty check --error-on-warning
mypy path/to/file.py          → ty check path/to/file.py
```

### Pyright → ty

```bash
pyright .                     → ty check
pyright path/to/file.py       → ty check path/to/file.py
```

## Common patterns

### Don't add ignore comments

Fix type errors instead of suppressing them. Only add ignore comments when
explicitly requested by the user. Use `ty: ignore`, not `type: ignore`, and
prefer rule-specific ignores:

```python
# Good: rule-specific ignore
x = undefined_var  # ty: ignore[possibly-unresolved-reference]

# Bad: blanket ty ignore
x = undefined_var  # ty: ignore

# Bad: tool agnostic blanket ignore
x = undefined_var  # type: ignore
```

## Documentation

For detailed information, read the official documentation:

- https://docs.astral.sh/ty/
