import math


def f2(x):
    result = 0
    if x < 80:
        result = math.tan(math.cos(pow(x, 2))) - (pow(x, 3)/4)
    elif 80 <= x < 117:
        result = pow((pow(x, 7) - math.tan(x) - 46), 3) + 76*pow(x, 2)
    elif 117 <= x < 158:
        result = x - pow(x, 4)
    elif 158 <= x < 232:
        result = pow(x, 3) + 98*pow(x, 6)
    else:
        math.sin(pow(x, 2) + 39*pow(x, 7) + 16) + pow(math.exp, (math.tan(x) + (pow(x, 6)/58)))
    return result
    
   
print("Задание 2")
    print(f2(97))
    print(f2(212))