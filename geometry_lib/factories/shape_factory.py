from typing import Union
from geometry_lib.shapes import Circle, Triangle, Rectangle
from geometry_lib.shapes.base import Shape


class ShapeFactory:
    """Factory for creating geometric shapes."""

    @staticmethod
    def create(*args: Union[float, float, float]) -> Shape:
        match args:
            case (radius,):
                return Circle(radius)
            case (a, b, c):
                return Triangle(a, b, c)
            case (width, height):
                return Rectangle(width, height)
            case _:
                raise ValueError(f"Invalid arguments for shape: {args}")