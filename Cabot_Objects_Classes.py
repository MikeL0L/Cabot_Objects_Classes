while True:
    import math

    class Circle:
        def __init__(self, radius):
            self.radius = radius

        def area(self):
            return math.pi * self.radius * self.radius


        def perimeter(self):
            return 2 * math.pi * self.radius

    rad_num = eval(input('Enter a Radius = ')) 
    circle = Circle(rad_num)

    area = round(circle.area(), 2)
    perimeter = round(circle.perimeter(), 2)

    print("Area of the Circle =", area)
    print("Perimeter of the Circle =", perimeter); print()

    choice = input('Do you want to make another claculation? '); print()
    if choice.lower() != 'yes':
        print('Thank you!'); print()
        break