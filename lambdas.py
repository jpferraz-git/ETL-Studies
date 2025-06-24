import random
from random import *

# double = lambda x: x * 2
# print(double(4))
#
# greater_number = lambda x, y: x if x > y else y
#
# zero = "03"
# zeros = lambda x: f"{x:03}"
#
# print(zeros(1))

def exercises():
    add_15 = lambda x: x + 15
    print(add_15(15))

    multiply = lambda x,y: x * y
    print(multiply(2,3))

    multiply_random = lambda x: x * randint(1,10)
    print(multiply_random(2))

    tuple_list = [("Adrian", 74), ("George", 88), ("Michael", 34), ("Lamar", 67)]
    lista = [sorted(tuple_list[1:]) for i in tuple_list ]

    print(lista)

    tuple_list.sort(key=lambda x: x[1])
    print(tuple_list)


exercises()