import math

def calculate_area(num_sides, side_length):
    area = (num_sides * side_length ** 2) / (4 * math.tan(math.pi / num_sides))
    return area
num_sides=int(input())
side_length = int(input())
area = calculate_area(num_sides, side_length)
print(area)