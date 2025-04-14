import pytest
from geometry_lib.factories import ShapeFactory
from geometry_lib.shapes import Circle, Triangle, Rectangle

class TestFactory:
    def test_create_circle(self):
        assert isinstance(ShapeFactory.create(5), Circle)
    
    def test_create_triangle(self):
        assert isinstance(ShapeFactory.create(3, 4, 5), Triangle)
    
    def test_create_rectangle(self):
        assert isinstance(ShapeFactory.create(4, 5), Rectangle)
    
    def test_invalid_creation(self):
        with pytest.raises(ValueError):
            ShapeFactory.create(1, 2, 3, 4)