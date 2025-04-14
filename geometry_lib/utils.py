from .shapes.base import Shape


def calculate_area(shape: Shape) -> float:
    """Calculate area without knowing concrete type."""
    return shape.area