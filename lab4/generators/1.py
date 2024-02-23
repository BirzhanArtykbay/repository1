def squares_generator(N):
    for i in range(1, N + 1):
        yield i * i


N = int(input("Enter a number: "))
squares = squares_generator(N)
for square in squares:
    print(square)