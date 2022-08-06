from math import sqrt

# объявление функции
def solve(a, b, c):
    x1, x2 = 0, 0
    D = b**2 - (4 * a * c)
    if D > 0:
        x1 = (b * -1 + sqrt(D)) / (2 * a)
        x2 = (b * -1 - sqrt(D)) / (2 * a)
    return min(x1, x2), max(x1, x2)

# считываем данные
a, b, c = int(input()), int(input()), int(input())

# вызываем функцию
x1, x2 = solve(a, b, c)
print(x1, x2)