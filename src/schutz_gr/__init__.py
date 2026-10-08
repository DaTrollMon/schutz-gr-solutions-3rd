"""Supporting code for solutions to Schutz, A First Course in General Relativity (3rd ed.).

Conventions follow Schutz: units with c = 1, metric signature (-, +, +, +),
and index 0 is the time component.
"""

from schutz_gr.special_relativity import (
    ETA,
    boost_matrix,
    gamma,
    interval,
)

__all__ = ["ETA", "boost_matrix", "gamma", "interval"]
