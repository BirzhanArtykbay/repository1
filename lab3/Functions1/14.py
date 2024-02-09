from math import pi
from itertools import permutations

def functions(gram):
    ounces = 28.3495231 * gram
    return ounces

def sphere_volume(radius):
    return (4/3) * pi * radius**3

def is_palindrome(word):
    word = word.replace(" ", "").lower()
    return word == word[::-1]

def unique_elements(input_list):
    unique_list = []
    for item in input_list:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list

def histogram(numbers):
    for num in numbers:
        print('*' * num)

if name == "__main__":
    a=int(input())
    print(functions(a))

    radius = 5
    print("Volume of the sphere with radius", radius, "is:", sphere_volume(radius))

    word = "madam"
    print("Is", word, "a palindrome?", is_palindrome(word))

    input_list = [1, 2, 2, 3, 4, 4, 5]
    print("Unique elements of the list:", unique_elements(input_list))

    numbers = [14, 9, 7]
    print("Histogram:")
    histogram(numbers)

