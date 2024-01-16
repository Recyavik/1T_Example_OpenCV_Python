def product(number):
    p = 1
    while number // 10 > 0:
        p *= (number % 10)
        number = number // 10
    return p

n = product(123)
print(n)

def product(number):
    p = 1
    for i in range(len(str(number))):
        p *= int(str(number)[i])
    return p

n = product(123)
print(n)