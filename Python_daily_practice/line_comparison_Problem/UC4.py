# use OOps methods , Implement Line and Point classes, and use methods to check equality and compare lines.
import math

def welcome_message():
    print("Welcome to Line Comparison Computation Program")

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def length(self):
        return math.sqrt((self.point2.x - self.point1.x) ** 2 + (self.point2.y - self.point1.y) ** 2)

    def equals(self, other_line):
        return self.length() == other_line.length()

    def compare_to(self, other_line):
        if self.length() > other_line.length():
            return "This line is greater"
        elif self.length() < other_line.length():
            return "This line is smaller"
        else:
            return "Both lines are equal"

if __name__ == "__main__":
    welcome_message()
    # Example points for two lines
    p1 = Point(0, 0)
    p2 = Point(3, 4)
    p3 = Point(1, 1)
    p4 = Point(4, 5)
    
    line1 = Line(p1, p2)
    line2 = Line(p3, p4)

    print(f"Length of line 1: {line1.length()}")
    print(f"Length of line 2: {line2.length()}")
    print(line1.compare_to(line2))
