import pytest
import math
from geometry_lib.shapes import Circle

class TestCircle:
    def test_area(self):
        assert Circle(1).area == math.pi
        assert Circle(2).area == 4 * math.pi
    
    def test_invalid_radius(self):
        with pytest.raises(ValueError):
            Circle(0)
        with pytest.raises(ValueError):
            Circle(-1)
    
    def test_not_right_angled(self):
        assert not Circle(5).is_right_angled()