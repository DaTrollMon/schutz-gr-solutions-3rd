"""Special-relativity helpers for Chapters 1-2 (c = 1, signature -+++)."""

from __future__ import annotations

import numpy as np
import sympy as sp

#: Minkowski metric eta_{alpha beta} = diag(-1, 1, 1, 1).
ETA = np.diag([-1.0, 1.0, 1.0, 1.0])


def gamma(v):
    """Lorentz factor 1 / sqrt(1 - v^2). Works with floats, arrays or sympy expressions."""
    if isinstance(v, sp.Basic):
        return 1 / sp.sqrt(1 - v**2)
    v = np.asarray(v, dtype=float)
    if np.any(np.abs(v) >= 1):
        raise ValueError("speed must satisfy |v| < 1 (c = 1)")
    return 1.0 / np.sqrt(1.0 - v**2)


def boost_matrix(v, axis: int = 1):
    """Lorentz boost Lambda^{alpha'}_{beta} for velocity v along the given spatial axis (1, 2 or 3).

    Returns a sympy Matrix if v is symbolic, otherwise a numpy array (Schutz eq. 2.3 for axis=1).
    """
    if axis not in (1, 2, 3):
        raise ValueError("axis must be 1, 2 or 3")
    symbolic = isinstance(v, sp.Basic)
    g = gamma(v)
    L = sp.eye(4) if symbolic else np.eye(4)
    L[0, 0] = g
    L[axis, axis] = g
    L[0, axis] = -v * g
    L[axis, 0] = -v * g
    return L


def interval(dx) -> float:
    """Spacetime interval Delta s^2 = eta_{ab} dx^a dx^b for a 4-vector (dt, dx, dy, dz)."""
    dx = np.asarray(dx, dtype=float)
    return float(dx @ ETA @ dx)


def interval_tx(dt, dx):
    """Delta s^2 = -dt^2 + dx^2 in a 1+1 dimensional diagram (works symbolically too)."""
    return -dt**2 + dx**2


def lorentz(t, x, v):
    """Coordinates (t_bar, x_bar) of event (t, x) for observer O_bar moving at v along +x (Schutz eq. 1.12).

    t_bar = gamma (t - v x),  x_bar = gamma (x - v t).  Works with numbers, arrays or sympy.
    """
    g = gamma(v)
    return g * (t - v * x), g * (x - v * t)


def inverse_lorentz(t_bar, x_bar, v):
    """Inverse of :func:`lorentz`: O's coordinates (t, x) of an event O_bar labels (t_bar, x_bar)."""
    g = gamma(v)
    return g * (t_bar + v * x_bar), g * (x_bar + v * t_bar)


def velocity_seen_by(w, v):
    """Velocity measured by O_bar (moving at v relative to O) of a body O sees moving at w.

    w_bar = (w - v) / (1 - w v)   (Schutz eq. 1.13 with v -> -v).
    """
    return (w - v) / (1 - w * v)
