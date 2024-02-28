import math
from threading import Timer

def calculate_square_root(number):
    result = math.sqrt(number)
    print(f"Square root of {number} after {ms} milliseconds is {result}")

num = int(input())
ms = int(input())

t = Timer(ms/1000, calculate_square_root(num))
