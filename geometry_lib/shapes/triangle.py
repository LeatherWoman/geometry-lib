import math
from typing_extensions import override
from .base import Shape


class Triangle(Shape):
    """Triangle shape implementation."""

    def __init__(self, a: float, b: float, c: float):
        sides = [a, b, c]
        if any(side <= 0 for side in sides):
            raise ValueError("All sides must be positive")
        if not self._is_valid(a, b, c):
            raise ValueError("Invalid triangle sides")

        self._sides = tuple(sorted(sides))  # type: ignore

    @property
    @override
    def area(self) -> float:
        p = sum(self._sides) / 2
        return math.sqrt(
            p * (p - self._sides[0]) * (p - self._sides[1]) * (p - self._sides[2])
        )

    @override
    def is_right_angled(self, tolerance: float = 1e-6) -> bool:
        a, b, c = self._sides
        return abs(a**2 + b**2 - c**2) < tolerance

    @staticmethod
    def _is_valid(a: float, b: float, c: float) -> bool:
        return (a + b > c) and (a + c > b) and (b + c > a)

    @property
    def sides(self) -> tuple[float, float, float]:
        return self._sides  # type: ignore