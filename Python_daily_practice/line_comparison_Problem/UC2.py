# Chek equality of 2 lines

import math

def welcome_message():
    print("Welcome to Line Comparison Computation Program")

def line_length(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def are_lines_equal(length1, length2):
    return length1 == length2

if __name__ == "__main__":
    welcome_message()
    # Example coordinates for two lines
    x1, y1 = 0, 0
    x2, y2 = 3, 4
    x3, y3 = 1, 1
    x4, y4 = 4, 5
    
    length1 = line_length(x1, y1, x2, y2)
    length2 = line_length(x3, y3, x4, y4)
    print(length1)
    print(length2)
    print(f"Are the two lines equal? {are_lines_equal(length1, length2)}")
