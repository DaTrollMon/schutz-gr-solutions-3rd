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

## Run in the cloud

**Google Colab** — every notebook has an *Open in Colab* button at the top (and in the table below). The notebook's first code cell installs the shared `schutz_gr` package from this repository if it isn't already present, so just run all cells. Colab uses its own Python (3.12 at present); the code supports Python ≥ 3.11.

> If this repository is **private**, Colab can only open it after you authorize it: in Colab choose *File → Open notebook → GitHub*, tick *Include private repos*, and sign in. The install cell also needs access, so for private use either make the repo public or use Codespaces.

**GitHub Codespaces** — [![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/DaTrollMon/schutz-gr-solutions-3rd) gives a full VS Code + Jupyter environment in the browser, set up exactly like the local one (Python 3.14.8 via `uv sync`, see `.devcontainer/`). Works for private repositories. Open any notebook and pick the `.venv` kernel.

## Chapter 1 notebooks — Special relativity

| Problem | Topic | |
|---|---|---|
| [1.1](Ch.1/Problem_1.1.ipynb) | SI → natural units ($c = 1$) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/DaTrollMon/schutz-gr-solutions-3rd/blob/main/Ch.1/Problem_1.1.ipynb) |
| [1.2](Ch.1/Problem_1.2.ipynb) | natural units ($c = 1$) → SI | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/DaTrollMon/schutz-gr-solutions-3rd/blob/main/Ch.1/Problem_1.2.ipynb) |
| [1.3](Ch.1/Problem_1.3.ipynb) | building a spacetime diagram | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/DaTrollMon/schutz-gr-solutions-3rd/blob/main/Ch.1/Problem_1.3.ipynb) |
| [1.4](Ch.1/Problem_1.4.ipynb) | writing out index sums | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/DaTrollMon/schutz-gr-solutions-3rd/blob/main/Ch.1/Problem_1.4.ipynb) |
| [1.5](Ch.1/Problem_1.5.ipynb) | one experiment, two observers | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/DaTrollMon/schutz-gr-solutions-3rd/blob/main/Ch.1/Problem_1.5.ipynb) |
| [1.6](Ch.1/Problem_1.6.ipynb) | only $M_{\alpha\beta} + M_{\beta\alpha}$ appears in Eq. (1.2) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/DaTrollMon/schutz-gr-solutions-3rd/blob/main/Ch.1/Problem_1.6.ipynb) |
| [1.7](Ch.1/Problem_1.7.ipynb) | the numbers $M_{\alpha\beta}$ for a general linear transformation | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/DaTrollMon/schutz-gr-solutions-3rd/blob/main/Ch.1/Problem_1.7.ipynb) |
| [1.8](Ch.1/Problem_1.8.ipynb) | deriving Eqs. (1.3), (1.4a) and (1.4b) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/DaTrollMon/schutz-gr-solutions-3rd/blob/main/Ch.1/Problem_1.8.ipynb) |
| [1.9](Ch.1/Problem_1.9.ipynb) | why the clock's world line in Fig. 1.7 is drawn as it is | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/DaTrollMon/schutz-gr-solutions-3rd/blob/main/Ch.1/Problem_1.9.ipynb) |
| [1.10](Ch.1/Problem_1.10.ipynb) | timelike, spacelike or null? | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/DaTrollMon/schutz-gr-solutions-3rd/blob/main/Ch.1/Problem_1.10.ipynb) |
| [1.11](Ch.1/Problem_1.11.ipynb) | the invariant hyperbolae share the light cone as asymptotes | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/DaTrollMon/schutz-gr-solutions-3rd/blob/main/Ch.1/Problem_1.11.ipynb) |
| [1.12](Ch.1/Problem_1.12.ipynb) | each observer sees the other's clocks run slow | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/DaTrollMon/schutz-gr-solutions-3rd/blob/main/Ch.1/Problem_1.12.ipynb) |
| [1.13](Ch.1/Problem_1.13.ipynb) | the half-life of a moving pion | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/DaTrollMon/schutz-gr-solutions-3rd/blob/main/Ch.1/Problem_1.13.ipynb) |
| [1.14](Ch.1/Problem_1.14.ipynb) | the low-velocity limits | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/DaTrollMon/schutz-gr-solutions-3rd/blob/main/Ch.1/Problem_1.14.ipynb) |
| [1.15](Ch.1/Problem_1.15.ipynb) | the ultra-relativistic limits | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/DaTrollMon/schutz-gr-solutions-3rd/blob/main/Ch.1/Problem_1.15.ipynb) |
| [1.16](Ch.1/Problem_1.16.ipynb) | time dilation and Lorentz contraction from the Lorentz transformation | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/DaTrollMon/schutz-gr-solutions-3rd/blob/main/Ch.1/Problem_1.16.ipynb) |
| [1.17](Ch.1/Problem_1.17.ipynb) | the pole-in-the-barn paradox | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/DaTrollMon/schutz-gr-solutions-3rd/blob/main/Ch.1/Problem_1.17.ipynb) |
| [1.18](Ch.1/Problem_1.18.ipynb) | velocity parameters (rapidity) add linearly | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/DaTrollMon/schutz-gr-solutions-3rd/blob/main/Ch.1/Problem_1.18.ipynb) |
| [1.19](Ch.1/Problem_1.19.ipynb) | the Lorentz transformation as a hyperbolic rotation | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/DaTrollMon/schutz-gr-solutions-3rd/blob/main/Ch.1/Problem_1.19.ipynb) |
| [1.20](Ch.1/Problem_1.20.ipynb) | the Lorentz transformation in matrix form | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/DaTrollMon/schutz-gr-solutions-3rd/blob/main/Ch.1/Problem_1.20.ipynb) |
| [1.21](Ch.1/Problem_1.21.ipynb) | timelike ⇒ same place in some frame; spacelike ⇒ same time in some frame | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/DaTrollMon/schutz-gr-solutions-3rd/blob/main/Ch.1/Problem_1.21.ipynb) |

## Chapter 2 notebooks — Vector analysis in special relativity

| Problem | Topic | |
|---|---|---|
| [2.1](Ch.2/Problem_2.1.ipynb) | practising the summation convention | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/DaTrollMon/schutz-gr-solutions-3rd/blob/main/Ch.2/Problem_2.1.ipynb) |
| [2.2](Ch.2/Problem_2.2.ipynb) | free and dummy indices | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/DaTrollMon/schutz-gr-solutions-3rd/blob/main/Ch.2/Problem_2.2.ipynb) |
| [2.3](Ch.2/Problem_2.3.ipynb) | prove Eq. (2.5) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/DaTrollMon/schutz-gr-solutions-3rd/blob/main/Ch.2/Problem_2.3.ipynb) |
| [2.4](Ch.2/Problem_2.4.ipynb) | vector arithmetic in components | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/DaTrollMon/schutz-gr-solutions-3rd/blob/main/Ch.2/Problem_2.4.ipynb) |
| [2.5](Ch.2/Problem_2.5.ipynb) | linear independence | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/DaTrollMon/schutz-gr-solutions-3rd/blob/main/Ch.2/Problem_2.5.ipynb) |
| [2.6](Ch.2/Problem_2.6.ipynb) | drawing basis vectors of three frames | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/DaTrollMon/schutz-gr-solutions-3rd/blob/main/Ch.2/Problem_2.6.ipynb) |
| [2.7](Ch.2/Problem_2.7.ipynb) | the basis vectors in index notation | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/DaTrollMon/schutz-gr-solutions-3rd/blob/main/Ch.2/Problem_2.7.ipynb) |
| [2.8](Ch.2/Problem_2.8.ipynb) | the zero vector, and equality of vectors | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/DaTrollMon/schutz-gr-solutions-3rd/blob/main/Ch.2/Problem_2.8.ipynb) |
| [2.9](Ch.2/Problem_2.9.ipynb) | the order of a double sum doesn't matter | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/DaTrollMon/schutz-gr-solutions-3rd/blob/main/Ch.2/Problem_2.9.ipynb) |
| [2.10](Ch.2/Problem_2.10.ipynb) | deriving the basis transformation, Eq. (2.13) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/DaTrollMon/schutz-gr-solutions-3rd/blob/main/Ch.2/Problem_2.10.ipynb) |
| [2.11](Ch.2/Problem_2.11.ipynb) | the inverse Lorentz transformation, entry by entry | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/DaTrollMon/schutz-gr-solutions-3rd/blob/main/Ch.2/Problem_2.11.ipynb) |
| [2.12](Ch.2/Problem_2.12.ipynb) | transforming a vector twice, and its invariant magnitude | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/DaTrollMon/schutz-gr-solutions-3rd/blob/main/Ch.2/Problem_2.12.ipynb) |
| [2.13](Ch.2/Problem_2.13.ipynb) | composing boosts in different directions | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/DaTrollMon/schutz-gr-solutions-3rd/blob/main/Ch.2/Problem_2.13.ipynb) |
| [2.14](Ch.2/Problem_2.14.ipynb) | reading a Lorentz matrix | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/DaTrollMon/schutz-gr-solutions-3rd/blob/main/Ch.2/Problem_2.14.ipynb) |
| [2.15](Ch.2/Problem_2.15.ipynb) | four-velocity components | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/DaTrollMon/schutz-gr-solutions-3rd/blob/main/Ch.2/Problem_2.15.ipynb) |
| [2.16](Ch.2/Problem_2.16.ipynb) | velocity addition from the four-velocity | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/DaTrollMon/schutz-gr-solutions-3rd/blob/main/Ch.2/Problem_2.16.ipynb) |
| [2.17](Ch.2/Problem_2.17.ipynb) | every unit future-timelike vector is a four-velocity | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/DaTrollMon/schutz-gr-solutions-3rd/blob/main/Ch.2/Problem_2.17.ipynb) |
| [2.18](Ch.2/Problem_2.18.ipynb) | orthogonality facts | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/DaTrollMon/schutz-gr-solutions-3rd/blob/main/Ch.2/Problem_2.18.ipynb) |
| [2.19](Ch.2/Problem_2.19.ipynb) | uniform acceleration and the 1 g rocket | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/DaTrollMon/schutz-gr-solutions-3rd/blob/main/Ch.2/Problem_2.19.ipynb) |
| [2.20](Ch.2/Problem_2.20.ipynb) | a particle drifting while it circles | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/DaTrollMon/schutz-gr-solutions-3rd/blob/main/Ch.2/Problem_2.20.ipynb) |
| [2.21](Ch.2/Problem_2.21.ipynb) | the hyperbolic world line | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/DaTrollMon/schutz-gr-solutions-3rd/blob/main/Ch.2/Problem_2.21.ipynb) |
| [2.22](Ch.2/Problem_2.22.ipynb) | four-momentum bookkeeping | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/DaTrollMon/schutz-gr-solutions-3rd/blob/main/Ch.2/Problem_2.22.ipynb) |
| [2.23](Ch.2/Problem_2.23.ipynb) | energy to fourth order in velocity | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/DaTrollMon/schutz-gr-solutions-3rd/blob/main/Ch.2/Problem_2.23.ipynb) |
| [2.24](Ch.2/Problem_2.24.ipynb) | pair annihilation needs two photons | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/DaTrollMon/schutz-gr-solutions-3rd/blob/main/Ch.2/Problem_2.24.ipynb) |
| [2.25](Ch.2/Problem_2.25.ipynb) | the Doppler shift at an angle | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/DaTrollMon/schutz-gr-solutions-3rd/blob/main/Ch.2/Problem_2.25.ipynb) |
| [2.26](Ch.2/Problem_2.26.ipynb) | the energy cost of the speed of light | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/DaTrollMon/schutz-gr-solutions-3rd/blob/main/Ch.2/Problem_2.26.ipynb) |
| [2.27](Ch.2/Problem_2.27.ipynb) | heat has inertia | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/DaTrollMon/schutz-gr-solutions-3rd/blob/main/Ch.2/Problem_2.27.ipynb) |
| [2.28](Ch.2/Problem_2.28.ipynb) | dot products are frame-independent | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/DaTrollMon/schutz-gr-solutions-3rd/blob/main/Ch.2/Problem_2.28.ipynb) |
| [2.29](Ch.2/Problem_2.29.ipynb) | the product rule for the dot product | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/DaTrollMon/schutz-gr-solutions-3rd/blob/main/Ch.2/Problem_2.29.ipynb) |
| [2.30](Ch.2/Problem_2.30.ipynb) | a cosmic ray seen from a rocket, two ways | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/DaTrollMon/schutz-gr-solutions-3rd/blob/main/Ch.2/Problem_2.30.ipynb) |
| [2.31](Ch.2/Problem_2.31.ipynb) | radiation pressure on a mirror | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/DaTrollMon/schutz-gr-solutions-3rd/blob/main/Ch.2/Problem_2.31.ipynb) |
| [2.32](Ch.2/Problem_2.32.ipynb) | Compton scattering | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/DaTrollMon/schutz-gr-solutions-3rd/blob/main/Ch.2/Problem_2.32.ipynb) |
| [2.33](Ch.2/Problem_2.33.ipynb) | inverse Compton scattering off a cosmic-ray proton | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/DaTrollMon/schutz-gr-solutions-3rd/blob/main/Ch.2/Problem_2.33.ipynb) |
| [2.34](Ch.2/Problem_2.34.ipynb) | the dot product is bilinear | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/DaTrollMon/schutz-gr-solutions-3rd/blob/main/Ch.2/Problem_2.34.ipynb) |
| [2.35](Ch.2/Problem_2.35.ipynb) | the boosted basis is orthonormal | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/DaTrollMon/schutz-gr-solutions-3rd/blob/main/Ch.2/Problem_2.35.ipynb) |

## Local setup

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
