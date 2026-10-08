import numpy as np
import sympy as sp

from schutz_gr import ETA, boost_matrix, gamma, interval


def test_gamma_at_rest():
    assert gamma(0.0) == 1.0


def test_boost_preserves_metric():
    L = boost_matrix(0.6)
    assert np.allclose(L.T @ ETA @ L, ETA)


def test_interval_invariant_under_boost():
    dx = np.array([3.0, 1.0, 2.0, -0.5])
    assert np.isclose(interval(dx), interval(boost_matrix(0.8, axis=2) @ dx))


def test_symbolic_boost():
    v = sp.symbols("v", real=True)
    L = boost_matrix(v)
    eta = sp.diag(-1, 1, 1, 1)
    assert sp.simplify(L.T * eta * L - eta) == sp.zeros(4)
