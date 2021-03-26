def compare_function(a, b):
    print(a is b)

class Shape():
    def __init__(self, w, l):
        self.width = w
        self.length = l

    def what_am_i(self):
        print("I am a shape")


class Rectangle(Shape):
    def __init__(self, w, l):
        self.width = w
        self.length = l

    def calculate_perimeter(self):
        return (2 * self.width) + (2 * self.length)

class Square(Shape):
    square_list = []
    def __init__(self, edge):
        self.s1 = edge
        self.square_list.append(self.s1)

    def __repr__(self):
        return """{} by {} by {} by {}""".format(self.s1, self.s1, self.s1, self.s1)


    def calculate_perimeter(self):
        return self.s1 * 4

rectangle = Rectangle(30, 40)
rectangle.what_am_i()
square = Square(40)
square.what_am_i()
print(Square(29))