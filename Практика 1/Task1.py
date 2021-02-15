import math


def f1(x, y, z):
    math_op_top = math.tan(z)-math.cos(y)
    math_op_bot = y - math.log(y)
    first_sqrt = math.sqrt(math_op_top / math_op_bot)
    math_op_top = pow(z, 7) - math.tan(y) - 46
    math_op_bot = math.cos(y) + pow(z, 4)
    second_op = math_op_top / math_op_bot
    second_sqrt = math.sqrt(pow(z, 6) + pow(x, 3))
    result = first_sqrt + second_op + second_sqrt
    return result
    
   
print("Задание 1")
    print(f1(73, 18, -21))
    print(f1(-48, 10, -30))