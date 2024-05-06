# LABORATORY ACTIVITY 4: DELA ROSA, SORIANO
# Introduction to OOP

class Circle: 

    total_count = 0

    def __init__(self, radius, color):
        self.radius = float(radius)
        self.color = str(color)
        Circle.total_count += 1

    def get_radius(self):
        print(f'The radius of the circle is {self.radius}.')

    def get_diameter(self): 
        diameter = 2*self.radius
        print(f'The diameter of the circle is {diameter}.')

    def calculate_area(self): 
        pi_value = 3.141592653589793238462643383279502884197
        area = pi_value*(self.radius)**2 
        print(f'The area of the circle is {area}.')

    def calculate_circumference(self): 
        pi_value = 3.141592653589793238462643383279502884197
        circumference = 2*pi_value*self.radius
        print(f'The circumference of the circle is {circumference}.')

    def get_color(self): 
        print(f'The color of the circle is {self.color}.')

    @staticmethod
    def set_color(new_color):
        print(f'The color of the circle has been changed to {new_color}.')

    @classmethod
    def update_total_count(cls):
        print(f'The total count of circle has been updated to {cls.total_count}.')

    @classmethod
    def get_circle_total_count(cls):
        print(f'Total number of circles created: {cls.total_count}.')

circle1 = Circle(2.0, "Blue")
print("\nCIRCLE 1")
print("SIZE")
circle1.get_radius()
circle1.get_diameter()
circle1.calculate_area()
circle1.calculate_circumference()
print("\nCOLOR")
circle1.get_color()
circle1.set_color("Orange")
print("\nNUMBER OF CIRCLES")
circle1.update_total_count()
circle1.get_circle_total_count()

print("\n------------------------------------------------------------")

circle2 = Circle(7.0, "Green")
print("\nCIRCLE 2")
print("SIZE")
circle2.get_radius()
circle2.get_diameter()
circle2.calculate_area()
circle2.calculate_circumference()
print("\nCOLOR")
circle2.get_color()
circle2.set_color("Orange")
print("\nNUMBER OF CIRCLES")
circle2.update_total_count()
circle2.get_circle_total_count()

print("\n------------------------------------------------------------")

circle3 = Circle(9.0, "Gray")
print("\nCIRCLE 3")
print("SIZE")
circle3.get_radius()
circle3.get_diameter()
circle3.calculate_area()
circle3.calculate_circumference()
print("\nCOLOR")
circle3.get_color()
circle3.set_color("Orange")
print("\nNUMBER OF CIRCLES")
circle3.update_total_count()
circle3.get_circle_total_count()

print("\n------------------------------------------------------------")

circle4 = Circle(11.0, "Violet")
print("\nCIRCLE 4")
print("SIZE")
circle4.get_radius()
circle4.get_diameter()
circle4.calculate_area()
circle4.calculate_circumference()
print("\nCOLOR")
circle4.get_color()
circle4.set_color("Orange")
print("\nNUMBER OF CIRCLES")
circle4.update_total_count()
circle4.get_circle_total_count()