def even_numbers_generator(N):
    for i in range(N + 1):
        if i % 2 == 0:
            yield i


N = int(input("Enter a number: "))

even_numbers = even_numbers_generator(N)

print(','.join(map(str, even_numbers)))
