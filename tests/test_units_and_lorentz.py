import math

import sympy as sp

from schutz_gr import (
    C_SCHUTZ,
    Quantity,
    interval_tx,
    inverse_lorentz,
    lorentz,
    to_natural,
    to_si,
    velocity_seen_by,
)


def test_joule_to_natural():
    q = to_natural(Quantity(10, kg=1, m=2, s=-2), c=C_SCHUTZ)
    assert (q.kg, q.m, q.s) == (1, 0, 0)
    assert math.isclose(q.value, 10 / 9e16)


def test_round_trip():
    pressure = Quantity(1e5, kg=1, m=-1, s=-2)
    back = to_si(to_natural(pressure), s=-2)
    assert (back.kg, back.m, back.s) == (1, -1, -2)
    assert math.isclose(back.value, 1e5)


def test_lorentz_inverse_and_interval():
    v = sp.Rational(1, 2)
    t, x = sp.symbols("t x", real=True)
    tb, xb = lorentz(t, x, v)
    t2, x2 = inverse_lorentz(tb, xb, v)
    assert sp.simplify(t2 - t) == 0 and sp.simplify(x2 - x) == 0
    assert sp.simplify(interval_tx(tb, xb) - interval_tx(t, x)) == 0


def test_velocity_seen_by():
    assert math.isclose(velocity_seen_by(1.0, 0.75), 1.0)  # light stays at c
    assert math.isclose(velocity_seen_by(0.75, 0.75), 0.0)
