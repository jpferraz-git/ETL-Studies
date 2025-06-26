import random
from random import *

from chardet.langcyrillicmodel import latin5_char_to_order_map


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
    tuple_list.sort(key=lambda x: x[1])
    print(tuple_list)

    listas = [i for i in range(1,11)]
    filtrado = filter(lambda x: x % 2 == 0, listas)
    for x in filtrado:
        print(x)

    double = map(lambda x: x * 2, listas)
    for i in double:
        print(f"{i / 2} Doubled is {i}")

    palavras = ['banana', 'abacaxi', 'uva', 'melancia']
    order = sorted(palavras, key=lambda x: x[-1])
    print(order)

    nomes = ['Carlos', 'Ana', 'Beatriz', 'João']
    bigger = max(nomes,key=lambda x: len(x) )
    print(bigger)

    squared = lambda x, y: (x + y) * 2 if x > y else (x - y) * 2
    print(squared(3,2))

    valores = [2, 4, 6, 8, 10]
    shd = map(lambda x: x / 2, filter(lambda y: y > 3, valores))
    for i in shd:
        print(i)

exercises()