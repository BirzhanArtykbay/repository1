def countdown(n):
    while n >= 0:
        yield n
        n -= 1


n = int(input("Enter a number: "))

print("Countdown from", n, "to 0:")
for number in countdown(n):
    print(number)