from geometry_lib import calculate_area, ShapeFactory

def test_polymorphic_area_calculation():
    shapes = [
        ShapeFactory.create(2),      # Circle
        ShapeFactory.create(3, 4, 5), # Triangle
        ShapeFactory.create(4, 5)    # Rectangle
    ]
    
    areas = [calculate_area(shape) for shape in shapes]
    assert round(areas[0], 2) == 12.57  # πr²
    assert areas[1] == 6.0              # Triangle
    assert areas[2] == 20.0             # Rectangle