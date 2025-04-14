from typing_extensions import override
from .base import Shape


class Rectangle(Shape):
    """Rectangle shape implementation."""

    def __init__(self, width: float, height: float):
        if width <= 0 or height <= 0:
            raise ValueError("Dimensions must be positive")
        self._width = width
        self._height = height

    @property
    @override
    def area(self) -> float:
        return self._width * self._height

    @override
    def is_right_angled(self) -> bool:
        return True

    @property
    def width(self) -> float:
        return self._width

    @property
    def height(self) -> float:
        return self._height