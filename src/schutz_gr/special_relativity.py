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


# --------------------------------------------------------------------------- Chapter 2 helpers

def minkowski_dot(A, B):
    """Scalar product A·B = −A⁰B⁰ + A¹B¹ + A²B² + A³B³ (Schutz eq. 2.26). Numbers, arrays or sympy."""
    if isinstance(A, sp.MatrixBase) or isinstance(B, sp.MatrixBase) or any(isinstance(a, sp.Basic) for a in list(A) + list(B)):
        return -A[0] * B[0] + A[1] * B[1] + A[2] * B[2] + A[3] * B[3]
    A = np.asarray(A, dtype=float)
    B = np.asarray(B, dtype=float)
    return float(A @ ETA @ B)


def four_velocity(v):
    """Four-velocity U = γ(1, v) for a 3-velocity v (sequence of 3 numbers or sympy expressions)."""
    v = list(v)
    v2 = sum(c * c for c in v)
    symbolic = any(isinstance(c, sp.Basic) for c in v)
    g = 1 / sp.sqrt(1 - v2) if symbolic else 1.0 / np.sqrt(1.0 - float(v2))
    if not symbolic and v2 >= 1:
        raise ValueError("speed must satisfy |v| < 1")
    out = [g] + [g * c for c in v]
    return sp.Matrix(out) if symbolic else np.array(out, dtype=float)


def boost_general(v):
    """Lorentz boost Λ^ᾱ_β to a frame moving with 3-velocity v (any direction, axes kept parallel).

    Λ⁰₀ = γ,  Λ⁰ᵢ = Λⁱ₀ = −γ vᵢ,  Λⁱⱼ = δᵢⱼ + (γ − 1) vᵢ vⱼ / v².
    Returns a sympy Matrix if any component is symbolic, else a numpy array.
    """
    v = list(v)
    symbolic = any(isinstance(c, sp.Basic) for c in v)
    v2 = sum(c * c for c in v)
    if v2 == 0:
        return sp.eye(4) if symbolic else np.eye(4)
    g = 1 / sp.sqrt(1 - v2) if symbolic else 1.0 / np.sqrt(1.0 - float(v2))
    L = sp.zeros(4, 4) if symbolic else np.zeros((4, 4))
    L[0, 0] = g
    for i in range(3):
        L[0, i + 1] = -g * v[i]
        L[i + 1, 0] = -g * v[i]
        for j in range(3):
            L[i + 1, j + 1] = (1 if i == j else 0) + (g - 1) * v[i] * v[j] / v2
    return L
