import math
n = 10
a = 0
for i in range (1, n+1):
    a += 1 / i ** 2
b = math.sqrt(6 * a)
print(b)
