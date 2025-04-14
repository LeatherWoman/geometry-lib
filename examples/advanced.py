from geometry_lib import ShapeFactory, calculate_area

# Using factory and polymorphism
shapes = [
    ShapeFactory.create(5),          # Circle
    ShapeFactory.create(3, 4, 5),   # Triangle
    ShapeFactory.create(4, 5)        # Rectangle
]

for shape in shapes:
    print(f"Shape: {type(shape).__name__}")
    print(f"Area: {calculate_area(shape):.2f}")
    print(f"Is right angled: {shape.is_right_angled()}")
    print()