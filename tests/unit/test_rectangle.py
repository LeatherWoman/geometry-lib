import pytest
from geometry_lib.shapes import Rectangle

class TestRectangle:
    def test_area(self):
        assert Rectangle(4, 5).area == 20
    
    def test_right_angled(self):
        assert Rectangle(4, 5).is_right_angled()
    
    def test_invalid_dimensions(self):
        with pytest.raises(ValueError):
            Rectangle(0, 5)
        with pytest.raises(ValueError):
            Rectangle(-1, 2)