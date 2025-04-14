import math
from typing_extensions import override
from .base import Shape


class Circle(Shape):
    """Circle shape implementation."""

    def __init__(self, radius: float):
        if radius <= 0:
            raise ValueError("Radius must be positive")
        self._radius = radius

    @property
    @override
    def area(self) -> float:
        return math.pi * self._radius ** 2

    @override
    def is_right_angled(self) -> bool:
        return False

    @property
    def radius(self) -> float:
        return self._radius