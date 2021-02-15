import math


def f3(i, j):
    sum_one = 0
    for a in range(1, i+1):
        for b in range(1, j+1):
            sum_one += math.tan(b) - math.cos(b)
    sum_one *= 33
    sum_two = 0
    for a in range(1, i+1):
        for b in range(1, j+1):
            sum_two += a + pow(b, 8)
    sum_two *= 13
    result = sum_one - sum_two
    return result
    
    
print("Задание 3")
    print(f3(84, 25))
    print(f3(86, 46))