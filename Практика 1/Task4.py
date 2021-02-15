import math


def f4(x):
    a1 = 2
    a2 = 5
    if x == 1:
        return a2
    elif x == 0:
        return a1
    for i in range(2, x+1):
        a3 = math.sin(a2)-math.sin(a1)-94
        a2 = a3
        a1 = a2
    return a2
    
    
print("Задание 4")
    print(f4(9))
    print(f4(2))