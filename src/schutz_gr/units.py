"""Conversions between SI units and Schutz's c = 1 ("natural") units.

Setting c = 1 identifies 1 s with c metres:

    1 = c = 299 792 458 m/s   =>   1 s = 299 792 458 m  (~ 3 x 10^8 m).

So an SI quantity  X kg^a m^b s^n  becomes, in units of kg and m,

    X kg^a m^b (c m)^n = X c^n  kg^a m^(b+n).

Going back to SI is the inverse: knowing the *physical* kind of quantity tells
you its SI time exponent n, and you divide by c^n.
"""

from __future__ import annotations

from dataclasses import dataclass

#: Speed of light in m/s (exact, by definition of the metre).
C_EXACT = 299_792_458.0
#: The rounded value Schutz uses in the text and answers.
C_SCHUTZ = 3.0e8


def _fmt_unit(kg: int, m: int, s: int = 0) -> str:
    parts = []
    for sym, p in (("kg", kg), ("m", m), ("s", s)):
        if p == 0:
            continue
        parts.append(sym if p == 1 else f"{sym}^{p}")
    return " ".join(parts) if parts else "(dimensionless)"


@dataclass(frozen=True)
class Quantity:
    """A value with SI-style exponents of kg, m and s."""

    value: float
    kg: int = 0
    m: int = 0
    s: int = 0

    @property
    def unit(self) -> str:
        return _fmt_unit(self.kg, self.m, self.s)

    def __str__(self) -> str:
        return f"{self.value:.3g} {self.unit}"


def to_natural(q: Quantity, c: float = C_EXACT) -> Quantity:
    """Convert an SI quantity to c = 1 units, expressed in kg and m only.

    X kg^a m^b s^n  ->  X c^n kg^a m^(b+n)
    """
    return Quantity(q.value * c**q.s, kg=q.kg, m=q.m + q.s, s=0)


def to_si(q: Quantity, s: int, c: float = C_EXACT) -> Quantity:
    """Convert a c = 1 quantity (kg^a m^b) back to SI, given the SI time exponent ``s``.

    The time exponent is fixed by what kind of quantity it is physically
    (e.g. s = -1 for a velocity, s = -2 for a pressure or an energy).
    X kg^a m^b  ->  X c^(-s) kg^a m^(b-s) s^s
    """
    if q.s != 0:
        raise ValueError("input must already be in c = 1 units (no seconds)")
    return Quantity(q.value / c**s, kg=q.kg, m=q.m - s, s=s)
