# UC1: Calculate the Length of a Line

import math

def welcome_message():
    print("Welcome to Line Comparison Computation Program")

def line_length(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

if __name__ == "__main__":
    welcome_message()
    # Example coordinates
    x1, y1 = 0, 0
    x2, y2 = 3, 4
    print(f"Length of the line: {line_length(x1, y1, x2, y2)}")
