from __future__ import annotations

import math
from typing import NamedTuple


class Point(NamedTuple):

    x: float
    y: float


class Line(NamedTuple):

    a: Point
    b: Point


class Triangle(NamedTuple):

    a: Point
    b: Point
    c: Point


def centroid(t: Triangle) -> Point:

    a, b, c = t
    return Point(
        (a.x + b.x + c.x)/3,
        (a.y + b.y + c.y)/3,
    )


def incenter(t: Triangle) -> Point:

    return Point(math.inf, math.inf)


def midpoint(p: Point, q: Point) -> Point:

    x = (p.x + q.x)/2
    y = (p.y + q.y)/2

    return Point(x, y)


def length(line: Line) -> float:

    a, b = line
    return ((a.x - b.x)**2 + (a.y - b.y)**2)**(1/2)


def slope(line: Line) -> float:

    a, b = line
    dx = a.x - b.x
    if dx == 0:
        return math.inf
    dy = a.y - b.y

    return dy/dx


def y_intercept(line: Line) -> float:

    a = line.a
    m = slope(line)

    if m == math.inf:
        return math.inf

    return a.y - m*a.x


def intersection(l1: Line, l2: Line) -> Point:

    m1, b1 = slope(l1), y_intercept(l1)
    m2, b2 = slope(l2), y_intercept(l2)

    if m1 == m2:
        raise ValueError('Parallel lines do not intersect')

    if m1 == math.inf:
        return Point(l1.a.x, m2*l1.a.x + b2)

    if m2 == math.inf:
        return Point(l2.a.x, m1*l2.a.x + b1)

    x = (b2 - b1)/(m1 - m2)
    y = m1*x + b1
    return Point(x, y)
