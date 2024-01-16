def factorial(n):
    if n == 1:
        return 1
    elif n == 0:
        return 0
    else:
        p = 1
        for i in range(1, int(n + 1)):
            p *= i
        return p
n = int(input())
print(factorial(n))