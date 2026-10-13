import numpy as np
import sympy as sp

from schutz_gr import ETA, boost_general, boost_matrix, four_velocity, minkowski_dot


def test_dot_and_four_velocity_normalised():
    U = four_velocity([0.5, 0.5, 0.5])
    assert np.allclose(U, [2, 1, 1, 1])
    assert np.isclose(minkowski_dot(U, U), -1)


def test_boost_general_matches_x_boost_and_is_lorentz():
    assert np.allclose(boost_general([0.6, 0, 0]), boost_matrix(0.6))
    L = boost_general([0.3, -0.2, 0.5])
    assert np.allclose(L.T @ ETA @ L, ETA)


def test_boost_general_takes_particle_to_rest():
    v = [0.5, 0.5, 0.5]
    assert np.allclose(boost_general(v) @ four_velocity(v), [1, 0, 0, 0])


def test_symbolic():
    a = sp.symbols("a", positive=True)
    U = four_velocity([a, 0, 0])
    assert sp.simplify(minkowski_dot(U, U)) == -1
