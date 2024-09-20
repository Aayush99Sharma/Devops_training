# main.py

import math

def welcome_message():
    print("Welcome to Line Comparison Computation Program")

def line_length(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def compare_lines(length1, length2):
    if length1 > length2:
        return "Line 1 is greater"
    elif length1 < length2:
        return "Line 2 is greater"
    else:
        return "Both lines are equal"

if __name__ == "__main__":
    welcome_message()
    # Example coordinates for two lines
    x1, y1 = 0, 0
    x2, y2 = 3, 4
    x3, y3 = 1, 1
    x4, y4 = 6, 8
    
    length1 = line_length(x1, y1, x2, y2)
    length2 = line_length(x3, y3, x4, y4)
    
    print(compare_lines(length1, length2))
