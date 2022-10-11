def f(x, y):
    return (x * y > A) and (x > y) and (x < 8)
for A in range(1, 100):
    if all(f(x, y) == 0 for x in range(1, 100) for y in range(1, 100)):
        print(A)
