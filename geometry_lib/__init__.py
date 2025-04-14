from .shapes import Circle, Triangle, Rectangle
from .factories.shape_factory import ShapeFactory
from .utils import calculate_area

__version__ = "0.2.0"
__all__ = ['Circle', 'Triangle', 'Rectangle', 'ShapeFactory', 'calculate_area']