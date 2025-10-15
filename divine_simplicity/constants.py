from __future__ import annotations

from dash import html

from divine_simplicity.geometry import Point
from divine_simplicity.geometry import Triangle

APP_TITLE = html.H1(
    html.Strong(
        className='hdg hdg_h1 mix-hdg_bold vr',
        children='Divine Simplicity',
    ),
)

EQUILATERAL_TRIANGLE = Triangle(
    Point(0, 0),
    Point(1, 0),
    Point(1/2, 3**(1/2)/2),
)
