def fibonacci():
    a = 0
    b = 1

    while True:
        yield a
        a, b = b, a + b


gen = fibonacci()

for i in range(10):
    print(next(gen))