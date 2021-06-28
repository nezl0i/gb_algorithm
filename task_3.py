"""
Задание 3 *.
Сделать профилировку для скриптов с рекурсией и сделать описание,
можно ли так профилировать и есть ли 'подводные камни' в профилировании?
Придумать как это решить!
Есть очень простое решение
"""

from random import randint
from memory_profiler import profile

"""
Step_1
"""


@profile
def recursive_reverse(number):
    if number == 0:
        return ''
    return f'{str(number % 10)}{recursive_reverse(number // 10)}'


num_100 = randint(1, 10000000)
recursive_reverse(num_100)

# На данном шаге попытаемся опредилить объем занимаемой памяти рекурсивной функции с помощью
# декоратора @profile библиотеки memory_profiler:
"""
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    17     18.1 MiB     18.1 MiB           1   @profile
    18                                         def recursive_reverse(number):
    19     18.1 MiB      0.0 MiB           1       if number == 0:
    20     18.1 MiB      0.0 MiB           1           return ''
    21                                             return f'{str(number % 10)}{recursive_reverse(number // 10)}'

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    17     18.1 MiB     18.1 MiB           2   @profile
    18                                         def recursive_reverse(number):
    19     18.1 MiB      0.0 MiB           2       if number == 0:
    20     18.1 MiB      0.0 MiB           1           return ''
    21     18.1 MiB      0.0 MiB           1       return f'{str(number % 10)}{recursive_reverse(number // 10)}'

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    17     18.1 MiB     18.1 MiB           3   @profile
    18                                         def recursive_reverse(number):
    19     18.1 MiB      0.0 MiB           3       if number == 0:
    20     18.1 MiB      0.0 MiB           1           return ''
    21     18.1 MiB      0.0 MiB           2       return f'{str(number % 10)}{recursive_reverse(number // 10)}'

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    17     18.1 MiB     18.1 MiB           4   @profile
    18                                         def recursive_reverse(number):
    19     18.1 MiB      0.0 MiB           4       if number == 0:
    20     18.1 MiB      0.0 MiB           1           return ''
    21     18.1 MiB      0.0 MiB           3       return f'{str(number % 10)}{recursive_reverse(number // 10)}'

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    17     18.1 MiB     18.1 MiB           5   @profile
    18                                         def recursive_reverse(number):
    19     18.1 MiB      0.0 MiB           5       if number == 0:
    20     18.1 MiB      0.0 MiB           1           return ''
    21     18.1 MiB      0.0 MiB           4       return f'{str(number % 10)}{recursive_reverse(number // 10)}'


Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    17     18.1 MiB     18.1 MiB           6   @profile
    18                                         def recursive_reverse(number):
    19     18.1 MiB      0.0 MiB           6       if number == 0:
    20     18.1 MiB      0.0 MiB           1           return ''
    21     18.1 MiB      0.0 MiB           5       return f'{str(number % 10)}{recursive_reverse(number // 10)}'

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    17     18.1 MiB     18.1 MiB           7   @profile
    18                                         def recursive_reverse(number):
    19     18.1 MiB      0.0 MiB           7       if number == 0:
    20     18.1 MiB      0.0 MiB           1           return ''
    21     18.1 MiB      0.0 MiB           6       return f'{str(number % 10)}{recursive_reverse(number // 10)}'

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    17     18.1 MiB     18.1 MiB           8   @profile
    18                                         def recursive_reverse(number):
    19     18.1 MiB      0.0 MiB           8       if number == 0:
    20     18.1 MiB      0.0 MiB           1           return ''
    21     18.1 MiB      0.0 MiB           7       return f'{str(number % 10)}{recursive_reverse(number // 10)}'

"""

# Здесь сразу выделяем пару моментов: 1. Это то, что сама функция простая и незатратная, поэтому мы не
# не можем определить объем затраченной памяти, 2. Это то, что замер происходит на каждом шаге рекурсии,
# когда сам профилировщик запускается заново. Попробуем добавить ресурсоемкие операции, чтобы попытаться опредилить
# расход памяти.

"""
Step_2
"""


@profile
def recursive_reverse(number):
    if number == 0:
        return ''

    c = [n*2 for n in range(10000)]
    array = [i*2 for i in range(1000)]

    return f'{str(number % 10)}{recursive_reverse(number // 10)}'


num_100 = randint(1, 10000000)
recursive_reverse(num_100)

"""
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
   107     21.5 MiB     21.5 MiB           1   @profile
   108                                         def recursive_reverse(number):
   109     21.5 MiB      0.0 MiB           1       if number == 0:
   110     21.5 MiB      0.0 MiB           1           return ''
   111                                         
   112                                             c = [n*2 for n in range(10000)]
   113                                             array = [i*2 for i in range(1000)]
   114                                         
   115                                             return f'{str(number % 10)}{recursive_reverse(number // 10)}'

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
   107     21.5 MiB     21.0 MiB           2   @profile
   108                                         def recursive_reverse(number):
   109     21.5 MiB      0.0 MiB           2       if number == 0:
   110     21.5 MiB      0.0 MiB           1           return ''
   111                                         
   112     21.2 MiB      0.3 MiB       10003       c = [n*2 for n in range(10000)]
   113     21.5 MiB      0.3 MiB        1003       array = [i*2 for i in range(1000)]
   114                                         
   115     21.5 MiB      0.0 MiB           1       return f'{str(number % 10)}{recursive_reverse(number // 10)}'

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
   107     21.5 MiB     20.4 MiB           3   @profile
   108                                         def recursive_reverse(number):
   109     21.5 MiB      0.0 MiB           3       if number == 0:
   110     21.5 MiB      0.0 MiB           1           return ''
   111                                         
   112     21.2 MiB      0.8 MiB       20006       c = [n*2 for n in range(10000)]
   113     21.5 MiB      0.3 MiB        2006       array = [i*2 for i in range(1000)]
   114                                         
   115     21.5 MiB      0.0 MiB           2       return f'{str(number % 10)}{recursive_reverse(number // 10)}'

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
   107     21.5 MiB     20.2 MiB           4   @profile
   108                                         def recursive_reverse(number):
   109     21.5 MiB      0.0 MiB           4       if number == 0:
   110     21.5 MiB      0.0 MiB           1           return ''
   111                                         
   112     21.2 MiB      1.0 MiB       30009       c = [n*2 for n in range(10000)]
   113     21.5 MiB      0.3 MiB        3009       array = [i*2 for i in range(1000)]
   114                                         
   115     21.5 MiB      0.0 MiB           3       return f'{str(number % 10)}{recursive_reverse(number // 10)}'

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
   107     21.5 MiB     19.7 MiB           5   @profile
   108                                         def recursive_reverse(number):
   109     21.5 MiB      0.0 MiB           5       if number == 0:
   110     21.5 MiB      0.0 MiB           1           return ''
   111                                         
   112     21.2 MiB      1.5 MiB       40012       c = [n*2 for n in range(10000)]
   113     21.5 MiB      0.3 MiB        4012       array = [i*2 for i in range(1000)]
   114                                         
   115     21.5 MiB     -0.1 MiB           4       return f'{str(number % 10)}{recursive_reverse(number // 10)}'

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
   107     21.5 MiB     19.1 MiB           6   @profile
   108                                         def recursive_reverse(number):
   109     21.5 MiB      0.0 MiB           6       if number == 0:
   110     21.5 MiB      0.0 MiB           1           return ''
   111                                         
   112     21.2 MiB      2.1 MiB       50015       c = [n*2 for n in range(10000)]
   113     21.5 MiB      0.3 MiB        5015       array = [i*2 for i in range(1000)]
   114                                         
   115     21.5 MiB     -0.2 MiB           5       return f'{str(number % 10)}{recursive_reverse(number // 10)}'

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
   107     21.5 MiB     18.9 MiB           7   @profile
   108                                         def recursive_reverse(number):
   109     21.5 MiB      0.0 MiB           7       if number == 0:
   110     21.5 MiB      0.0 MiB           1           return ''
   111                                         
   112     21.2 MiB      2.3 MiB       60018       c = [n*2 for n in range(10000)]
   113     21.5 MiB      0.3 MiB        6018       array = [i*2 for i in range(1000)]
   114                                         
   115     21.5 MiB     -0.3 MiB           6       return f'{str(number % 10)}{recursive_reverse(number // 10)}'


Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
   107     21.5 MiB     18.4 MiB           8   @profile
   108                                         def recursive_reverse(number):
   109     21.5 MiB      0.0 MiB           8       if number == 0:
   110     21.5 MiB      0.0 MiB           1           return ''
   111                                         
   112     21.2 MiB      2.8 MiB       70021       c = [n*2 for n in range(10000)]
   113     21.5 MiB      0.3 MiB        7021       array = [i*2 for i in range(1000)]
   114                                         
   115     21.5 MiB     -0.4 MiB           7       return f'{str(number % 10)}{recursive_reverse(number // 10)}'

"""

# На втором шаге мы добавили две функции LC, и уже видим, что происходит расход памяти. Однако
# по результатам профилировщика абсолютно не понятно, какой реальный объем памяти используюется,
# т.к. на каждом шаге рекурсии декоратор запускает замер заново. Можно сделать вывод, что профилирование
# памяти рекурсивных функций таким способом сделать невозможно, да и такой подход будет крайне неправильным.
# Единственный вариант, который я считаю даст представление об объеме занимаемой памяти рекурсивной функции, это
# вызывать рекурсивную функцию из другой функции, над которой и проводить профилирование с помощью @profile.
# Разберем это на шаге 3

"""
Step_3
"""


def recursive_reverse(number):
    if number == 0:
        return ''
    c = [n*2 for n in range(10000)]
    array = [i*2 for i in range(1000)]
    return f'{str(number % 10)}{recursive_reverse(number // 10)}'


num_100 = randint(1, 10000000)


@profile
def func(num):
    recursive_reverse(num)


func(num_100)

"""
Line #    Mem usage    Increment  Occurrences   Line Contents
============================================================
   245     18.2 MiB     18.2 MiB           1   @profile
   246                                         def func(num):
   247     19.4 MiB      1.2 MiB           1       recursive_reverse(num)
"""

# На этом шаге мы произвели профилирование памяти функции, которая вызывает рекурсивную функцию.
# Я не могу с уверенностью сказать, что данный подход верен, но мы видим результат, который приближен
# к действительности.
