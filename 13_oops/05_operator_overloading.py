# vector example
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def sum(self, p):
        return Point((self.x + p.x), (self.y + p.y))

    def print_point(self):
        print(f"X is {self.x} and y is {self.y}")

    def __add__(self, p):
        return Point(self.x + p.x, self.y + p.y)


p1 = Point(3, 2)
p2 = Point(4, 3)

# p = p1.sum(p2)  # returns new point which is sum of p1 & p2

# if we need to use it as p=p1+p2  use operator overloading by adding __add__ func
p = p1 + p2

p.print_point()
