from __future__ import annotations

import math

import pytest

from divine_simplicity.geometry import centroid
from divine_simplicity.geometry import get_coordinates
from divine_simplicity.geometry import intersection
from divine_simplicity.geometry import length
from divine_simplicity.geometry import Line
from divine_simplicity.geometry import midpoint
from divine_simplicity.geometry import Point
from divine_simplicity.geometry import slope
from divine_simplicity.geometry import Triangle
from divine_simplicity.geometry import y_intercept


def test_get_coordinates_on_point():

    p = Point(0, 0)
    expected = ((0,), (0,))

    assert get_coordinates(p) == expected


def test_get_coordinates_on_sequence():

    t = Triangle(
        Point(0, 0),
        Point(5, 0),
        Point(2.5, 2.5),
    )

    expected = (
        (0, 5, 2.5, 0),
        (0, 0, 2.5, 0),
    )

    assert get_coordinates(t) == expected


@pytest.mark.parametrize(
    ('t', 'expected'),
    (
        (
            Triangle(
                Point(0, 0),
                Point(5, 0),
                Point(0, 5),
            ),
            Point(5/3, 5/3),
        ),
        (
            Triangle(
                Point(1, 2),
                Point(5, 3),
                Point(3, 1),
            ),
            Point(3, 2),
        ),
    ),
)
def test_centroid(t, expected):

    assert centroid(t) == expected


@pytest.mark.parametrize(
    ('line', 'expected'),
    (
        (Line(Point(0, 0), Point(1, 0)), 0),
        (Line(Point(1, 1), Point(2, 2)), 0),
        (Line(Point(2, 0), Point(1, 1)), 2),
        (Line(Point(1, 2), Point(1, 3)), math.inf),
        (Line(Point(-1, 0), Point(1, 0)), 0),
    ),
)
def test_y_intercept(line, expected):

    assert y_intercept(line) == expected


def test_intersection_parallel():

    with pytest.raises(ValueError):
        intersection(
            Line(Point(0, 0), Point(1, 1)),
            Line(Point(0, 1), Point(1, 2)),
        )

    with pytest.raises(ValueError):
        intersection(
            Line(Point(0, 1), Point(1, 1)),
            Line(Point(0, 1), Point(1, 1)),
        )


@pytest.mark.parametrize(
    ('l1', 'l2', 'expected'),
    (
        (
            Line(Point(-1, 0), Point(1, 0)),
            Line(Point(0, -1), Point(0, 1)),
            Point(0, 0),
        ),
        (
            Line(Point(0, 0), Point(5, 5)),
            Line(Point(5, 0), Point(0, 5)),
            Point(2.5, 2.5),
        ),

    ),
)
def test_intersection(l1, l2, expected):

    assert intersection(l1, l2) == expected


@pytest.mark.parametrize(
    ('line', 'expected'),
    (
        (Line(Point(0, 0), Point(1, 0)), 0),
        (Line(Point(0, 0), Point(0, 1)), math.inf),
        (Line(Point(0, 0), Point(1, 1)), 1),
        (Line(Point(-1, -1), Point(2, 3)), 4/3),
        (Line(Point(-1, 0), Point(1, 0)), 0),
    ),
)
def test_slope(line, expected):

    assert slope(line) == expected


@pytest.mark.parametrize(
    ('line', 'expected'),
    (
        (Line(Point(0, 0), Point(0, 1)), 1),
        (Line(Point(0, 0), Point(0, 0)), 0),
        (Line(Point(1, 3), Point(2, 5)), 5**(1/2)),
    ),
)
def test_line(line, expected):

    assert length(line) == expected


@pytest.mark.parametrize(
    ('p', 'q', 'expected'),
    (
        (Point(0, 0), Point(1, 1), Point(0.5, 0.5)),
        (Point(1, 1), Point(1, 1), Point(1, 1)),
        (Point(-1, -1), Point(1, 1), Point(0, 0)),
    ),
)
def test_midpoint(p, q, expected):

    assert midpoint(p, q) == expected
