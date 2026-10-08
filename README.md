# Schutz GR Solutions (3rd ed.)

Worked solutions to problems from Bernard Schutz, *A First Course in General Relativity*, 3rd edition, as Jupyter notebooks.

## Layout

```
Ch.1/            Chapter 1 notebooks — Special relativity
Ch.2/            Chapter 2 notebooks — Vector analysis in special relativity
src/schutz_gr/   Shared Python code imported by the notebooks
tests/           Tests for the shared code
```

Notebooks hold the solutions; anything reusable across problems goes in `src/schutz_gr/`.

## Setup

The environment is managed with [uv](https://docs.astral.sh/uv/). Python 3.14.8 is pinned in `.python-version`, and uv will download it if needed.

```bash
uv sync                # create .venv with Python 3.14.8, install deps + schutz_gr (editable)
uv run jupyter lab     # notebooks in Ch.x/ can `import schutz_gr`
```

To use the environment from VS Code or another Jupyter front end, select the `.venv` interpreter, or register a named kernel:

```bash
uv run python -m ipykernel install --user --name schutz-gr --display-name "Python 3.14 (schutz-gr)"
```

Adding dependencies:

```bash
uv add <package>             # runtime dependency
uv add --dev <package>       # dev-only tool
```

## Tests

```bash
uv run pytest
```
