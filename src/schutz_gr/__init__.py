"""Supporting code for solutions to Schutz, A First Course in General Relativity (3rd ed.).

Conventions follow Schutz: units with c = 1, metric signature (-, +, +, +),
and index 0 is the time component.

Modules
-------
special_relativity : metric, gamma, boosts, Lorentz transformation, velocity addition
units              : SI <-> c = 1 conversions
diagrams           : dark-themed matplotlib spacetime diagrams (import explicitly)
"""

from schutz_gr.special_relativity import (
    ETA,
    boost_matrix,
    gamma,
    interval,
    boost_general,
    four_velocity,
    interval_tx,
    inverse_lorentz,
    minkowski_dot,
    lorentz,
    velocity_seen_by,
)
from schutz_gr.units import C_EXACT, C_SCHUTZ, Quantity, to_natural, to_si

__all__ = [
    "ETA",
    "boost_matrix",
    "gamma",
    "interval",
    "interval_tx",
    "minkowski_dot",
    "four_velocity",
    "boost_general",
    "inverse_lorentz",
    "lorentz",
    "velocity_seen_by",
    "C_EXACT",
    "C_SCHUTZ",
    "Quantity",
    "to_natural",
    "to_si",
]
