class Orange:
    def __init__(self, w, c):
        self.weight = w
        self.colour = c
        self.mold = 0
        print("Created!")

    def rot(self, days, temp):
        self.mold = days * temp

orange_one = Orange(2, "orange")
"""
orange_two = Orange(9, "light orange")
orange_three = Orange(7, "dark orange")
"""

def print_orange(o):
    print(o.weight)
    print(o.colour)
    print(o.mold)
    print("")

print_orange(orange_one)
orange_one.rot(10, 98)
print_orange(orange_one)
