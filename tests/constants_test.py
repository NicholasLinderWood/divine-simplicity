from __future__ import annotations

from divine_simplicity.constants import EQUILATERAL_TRIANGLE
from divine_simplicity.geometry import length
from divine_simplicity.geometry import Line


def test_equilateral_triangle():

    a, b, c = EQUILATERAL_TRIANGLE
    A = Line(a, b)
    B = Line(b, c)
    C = Line(c, a)

    assert length(A) == length(B)
    assert length(B) == length(C)
    assert length(C) == length(A)
