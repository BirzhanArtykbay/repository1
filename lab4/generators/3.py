def divisible_by_3_and_4_generator(n):
    for i in range(n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

# Example usage:
n = int(input("Enter a number: "))
numbers_divisible_by_3_and_4 = divisible_by_3_and_4_generator(n)

print("Numbers divisible by both 3 and 4 between 0 and", n, ":", end=" ")
for num in numbers_divisible_by_3_and_4:
    print(num, end=" ")