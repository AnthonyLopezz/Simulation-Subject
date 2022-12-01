a = int(input('Input N: '))
def fib(n):
    a, b = 0, 1
    for i in range(n+2):
        yield a
        a, b = b, a + b
print(list(fib(a)))