"""Dark-themed spacetime (Minkowski) diagrams with matplotlib.

Conventions: c = 1, x horizontal, t vertical, equal scales so light rays are at 45 degrees.

Usage::

    from schutz_gr.diagrams import SpacetimeDiagram, COLORS
    d = SpacetimeDiagram(xlim=(-3, 3), tlim=(-3, 3), title="Problem 3")
    d.light_cone()
    d.boosted_axes(0.5)
    d.world_line(lambda t: 1 + 0 * t, label="clock at x = 1")
    d.show()
"""

from __future__ import annotations

from collections.abc import Callable

import matplotlib.pyplot as plt
import numpy as np

from schutz_gr.special_relativity import gamma, inverse_lorentz

COLORS = {
    "bg": "#0d0f14",
    "panel": "#12151c",
    "grid": "#1e2230",
    "axis": "#4a5568",
    "text": "#e8e2d5",
    "muted": "#a09880",
    "teal": "#7eb8c9",
    "amber": "#f4a261",
    "green": "#a8d8a8",
    "gold": "#f9d56e",
    "violet": "#b39ddb",
    "rose": "#ef8fa0",
    "grey": "#6b7280",
}


class SpacetimeDiagram:
    """A t-vs-x diagram in observer O's coordinates."""

    def __init__(
        self,
        xlim=(-3.0, 3.0),
        tlim=(-3.0, 3.0),
        title: str | None = None,
        size: float = 7.0,
        ax=None,
        observer: str = "O",
        tlabel: str = "t",
        xlabel: str = "x",
    ):
        self.xlim, self.tlim = xlim, tlim
        if ax is None:
            w = xlim[1] - xlim[0]
            h = tlim[1] - tlim[0]
            self.fig, self.ax = plt.subplots(figsize=(size, size * h / w))
        else:
            self.fig, self.ax = ax.figure, ax
        self.fig.patch.set_facecolor(COLORS["bg"])
        ax = self.ax
        ax.set_facecolor(COLORS["panel"])
        ax.set_xlim(*xlim)
        ax.set_ylim(*tlim)
        ax.set_aspect("equal")
        for side in ax.spines.values():
            side.set_visible(False)
        ax.tick_params(colors=COLORS["grey"], labelsize=8)
        ax.set_xticks(np.arange(np.ceil(xlim[0]), np.floor(xlim[1]) + 1))
        ax.set_yticks(np.arange(np.ceil(tlim[0]), np.floor(tlim[1]) + 1))
        ax.grid(color=COLORS["grid"], lw=0.8)
        ax.set_axisbelow(True)
        # O's axes through the origin
        ax.axhline(0, color=COLORS["axis"], lw=1.4, zorder=1)
        ax.axvline(0, color=COLORS["axis"], lw=1.4, zorder=1)
        ax.text(0.08, tlim[1] - 0.12, f"${tlabel}$ (m)", color=COLORS["teal"], fontsize=13, va="top")
        ax.text(xlim[1] - 0.08, 0.1, f"${xlabel}$ (m)", color=COLORS["teal"], fontsize=13, ha="right")
        ax.text(-0.1, -0.1, observer, color=COLORS["grey"], fontsize=9, ha="right", va="top")
        if title:
            ax.set_title(title, color=COLORS["text"], fontsize=12, loc="left", pad=10)
        self._legend_handles = []

    # ------------------------------------------------------------------ primitives
    def _t_range(self, n=400):
        return np.linspace(self.tlim[0], self.tlim[1], n)

    def _x_range(self, n=400):
        return np.linspace(self.xlim[0], self.xlim[1], n)

    def line(self, x, t, color="text", label=None, lw=2.0, ls="-", alpha=1.0, zorder=3):
        (h,) = self.ax.plot(x, t, color=COLORS.get(color, color), lw=lw, ls=ls, alpha=alpha,
                            label=label, zorder=zorder, solid_capstyle="round")
        if label:
            self._legend_handles.append(h)
        return h

    def world_line(self, x_of_t: Callable, t_range=None, **kw):
        """World line given as x(t)."""
        t = self._t_range() if t_range is None else np.linspace(*t_range, 400)
        return self.line(x_of_t(t), t, **kw)

    def simultaneity_line(self, t_of_x: Callable, x_range=None, **kw):
        """A curve given as t(x), e.g. a line of simultaneity."""
        x = self._x_range() if x_range is None else np.linspace(*x_range, 400)
        return self.line(x, t_of_x(x), **kw)

    def event(self, t, x, name=None, color="text", offset=(6, 6), size=36, note=None):
        self.ax.scatter([x], [t], s=size, color=COLORS.get(color, color), zorder=6,
                        edgecolor=COLORS["bg"], linewidth=0.8)
        if name or note:
            txt = name or ""
            if note:
                txt = f"{txt}  {note}" if txt else note
            self.ax.annotate(txt, (x, t), xytext=offset, textcoords="offset points",
                             color=COLORS.get(color, color), fontsize=10, zorder=7)

    def text(self, t, x, s, color="muted", **kw):
        kw.setdefault("fontsize", 9)
        self.ax.text(x, t, s, color=COLORS.get(color, color), zorder=7, **kw)

    # ------------------------------------------------------------------ structures
    def light_cone(self, t0=0.0, x0=0.0, label="light cone (Δs² = 0)", color="gold", shade=True):
        x = self._x_range()
        self.line(x, t0 + (x - x0), color=color, lw=1.2, ls="--", alpha=0.8, label=label)
        self.line(x, t0 - (x - x0), color=color, lw=1.2, ls="--", alpha=0.8)
        if shade:
            c = COLORS.get(color, color)
            self.ax.fill_between(x, t0 + np.abs(x - x0), self.tlim[1], color=c, alpha=0.05, zorder=0)
            self.ax.fill_between(x, self.tlim[0], t0 - np.abs(x - x0), color=c, alpha=0.05, zorder=0)

    def boosted_axes(self, v, color="amber", names=("t̄", "x̄"), ticks: int = 0, label=None):
        """Axes of an observer moving at v (origins coincide): t̄ axis x = v t, x̄ axis t = v x.

        ``ticks`` draws calibration ticks at t̄ = ±1..±ticks and x̄ = ±1..±ticks,
        i.e. at the events (γn, γvn) and (γvn, γn) where the axes cross the invariant hyperbolae.
        """
        t = self._t_range()
        x = self._x_range()
        lab = label if label is not None else f"Ō axes (v = {v:g})"
        self.line(v * t, t, color=color, lw=1.8, label=lab)
        self.line(x, v * x, color=color, lw=1.8)
        # place axis names near the top / right edge
        # axis names sit just *outside* the acute angle between the two axes, clear of tick labels
        tt = self.tlim[1] * 0.92
        self.ax.text(v * tt - 0.12, tt, names[0], color=COLORS.get(color, color), fontsize=14,
                     ha="right", va="center")
        xx = self.xlim[1] * 0.92
        self.ax.text(xx, v * xx - 0.12, names[1], color=COLORS.get(color, color), fontsize=14,
                     ha="center", va="top")
        if ticks:
            g = float(gamma(v))
            for n in range(-ticks, ticks + 1):
                if n == 0:
                    continue
                for tb, xb in ((n, 0), (0, n)):
                    te, xe = inverse_lorentz(tb, xb, v)
                    if self.xlim[0] < xe < self.xlim[1] and self.tlim[0] < te < self.tlim[1]:
                        self.ax.scatter([xe], [te], s=22, marker="o", color=COLORS.get(color, color),
                                        edgecolor=COLORS["bg"], zorder=6)
                        self.ax.annotate(str(n), (xe, te), xytext=(5, -10), textcoords="offset points",
                                         color=COLORS.get(color, color), fontsize=8)
            del g

    def hyperbola(self, s2, color="violet", label=None, lw=1.6, ls="-"):
        """Invariant hyperbola  -t² + x² = s2 (both branches)."""
        if s2 < 0:  # timelike: t = ±sqrt(x² - s2)
            x = self._x_range(800)
            t = np.sqrt(x**2 - s2)
            self.line(x, t, color=color, lw=lw, ls=ls, label=label)
            self.line(x, -t, color=color, lw=lw, ls=ls)
        elif s2 > 0:  # spacelike: x = ±sqrt(t² + s2)
            t = self._t_range(800)
            x = np.sqrt(t**2 + s2)
            self.line(x, t, color=color, lw=lw, ls=ls, label=label)
            self.line(-x, t, color=color, lw=lw, ls=ls)
        else:
            self.light_cone(label=label or "Δs² = 0", color=color, shade=False)

    # ------------------------------------------------------------------ output
    def legend(self, loc="lower right", **kw):
        if not self._legend_handles:
            return
        leg = self.ax.legend(handles=self._legend_handles, loc=loc, fontsize=8.5, frameon=True, **kw)
        leg.get_frame().set_facecolor(COLORS["bg"])
        leg.get_frame().set_edgecolor(COLORS["grid"])
        for txt in leg.get_texts():
            txt.set_color(COLORS["text"])

    def show(self, legend=True, **kw):
        if legend:
            self.legend(**kw)
        self.fig.tight_layout()
        plt.show()
