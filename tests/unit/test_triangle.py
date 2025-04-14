import pytest
from geometry_lib.shapes import Triangle

class TestTriangle:
    def test_area(self):
        assert Triangle(3, 4, 5).area == 6.0
    
    def test_right_angled(self):
        assert Triangle(3, 4, 5).is_right_angled()
        assert not Triangle(3, 4, 6).is_right_angled()
    
    def test_invalid_sides(self):
        with pytest.raises(ValueError):
            Triangle(1, 1, 3)
        with pytest.raises(ValueError):
            Triangle(-1, 2, 2)