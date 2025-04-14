from geometry_lib import Circle, Triangle, Rectangle

# Direct usage
circle = Circle(5)
print(f"Circle area: {circle.area:.2f}")

triangle = Triangle(3, 4, 5)
print(f"Triangle area: {triangle.area:.2f}")
print(f"Is right angled: {triangle.is_right_angled()}")

rectangle = Rectangle(4, 5)
print(f"Rectangle area: {rectangle.area:.2f}")