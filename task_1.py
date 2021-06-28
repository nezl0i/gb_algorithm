"""
Задание 1.

Выполните профилирование памяти в скриптах
Проанализировать результат и определить программы с
наиболее эффективным использованием памяти.

Примечание: Для анализа возьмите любые 3-5 ваших РАЗНЫХ скриптов!
(хотя бы 3 разных для получения оценки отл).
На каждый скрипт вы должны сделать как минимум по две реализации.

Можно взять только домашние задания с курса Основ
или с текущего курса Алгоритмов

Результаты профилирования добавьте в виде комментариев к коду.
Обязательно сделайте аналитику (что с памятью в ваших скриптах, в чем ваша оптимизация и т.д.)

ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО

Попытайтесь дополнительно свой декоратор используя ф-цию memory_usage из memory_profiler
С одновременным замером времени (timeit.default_timer())!
"""
from memory_profiler import profile
import time
import numpy as np
import requests

# Example_1
# -------------------------------------------------
# Данный пример демонстрирует создание 2-х списков с помощью LC.
# Третий список - LC из суммы первых двух списков.
# И в итоге выводим сумму элементов третьего списка
# Проведем профилировку памяти:


@profile
def main_func1():
    import random
    arr1 = [random.randint(1, 10) for i in range(100000)]
    arr2 = [random.randint(1, 10) for i in range(100000)]
    arr3 = [arr1[i] + arr2[i] for i in range(100000)]
    total = sum(arr3)
    print(total)


"""

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    34     18.0 MiB     18.0 MiB           1   @profile
    35                                         def main_func():
    36     18.2 MiB      0.2 MiB           1       import random
    37     19.0 MiB      0.8 MiB      100003       arr1 = [random.randint(1, 10) for i in range(100000)]
    38     19.8 MiB      0.8 MiB      100003       arr2 = [random.randint(1, 10) for i in range(100000)]
    39     20.5 MiB      0.8 MiB      100003       arr3 = [arr1[i]+arr2[i] for i in range(100000)]
    40     20.5 MiB      0.0 MiB           1       total = sum(arr3)
    41     20.5 MiB      0.0 MiB           1       print(total)
    
Результаты замеров говорят о том, что все три созданных объекта занимают память. Проведем оптимизацию
путем удаления объектов из оперативной памяти, до завершения программы

"""


@profile
def main_func1():
    import random
    arr1 = [random.randint(1, 10) for i in range(100000)]
    arr2 = [random.randint(1, 10) for i in range(100000)]
    arr3 = [arr1[i] + arr2[i] for i in range(100000)]
    del arr1
    del arr2
    total = sum(arr3)
    del arr3
    print(total)


"""
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    61     18.1 MiB     18.1 MiB           1   @profile
    62                                         def main_func():
    63     18.3 MiB      0.3 MiB           1       import random
    64     19.1 MiB      0.8 MiB      100003       arr1 = [random.randint(1, 10) for i in range(100000)]
    65     19.9 MiB      0.8 MiB      100003       arr2 = [random.randint(1, 10) for i in range(100000)]
    66     20.7 MiB      0.8 MiB      100003       arr3 = [arr1[i]+arr2[i] for i in range(100000)]
    67     20.1 MiB     -0.6 MiB           1       del arr1
    68     19.3 MiB     -0.8 MiB           1       del arr2
    69     19.3 MiB      0.0 MiB           1       total = sum(arr3)
    70     18.6 MiB     -0.8 MiB           1       del arr3
    71     18.6 MiB      0.0 MiB           1       print(total)
    
Результат замеров говорит о том, что все три объекта были удалены в момент их ненадобности, тем самым 
высбоводив оперативную память. 
"""

# Example_ 2
# Функция вычисления среднеарифметического значения массива с помощью функции random


@profile
def random_generator():
    arr1 = np.random.randint(1, 100, size=(1000, 1000))
    avg = arr1.mean()
    return avg


def main_func():
    random_generator()


"""

============================================================
   100     33.0 MiB     33.0 MiB           1   @profile
   101                                         def random_generator():
   102     40.7 MiB      7.6 MiB           1       arr1 = np.random.randint(1, 100, size=(1000, 1000))
   103     40.9 MiB      0.3 MiB           1       avg = arr1.mean()
   104     40.9 MiB      0.0 MiB           1       return avg
   
Снова видем занимаемое место в памяти массива arr1. Оптимизируем память, удалив объект с помощью функции del
"""


@profile
def random_generator2():
    arr1 = np.random.randint(1, 100, size=(1000, 1000))

    avg = arr1.mean()
    del arr1
    return avg


def main_func2():
    random_generator2()

"""

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
   123     32.9 MiB     32.9 MiB           1   @profile
   124                                         def random_generator2():
   125     40.6 MiB      7.7 MiB           1       arr1 = np.random.randint(1, 100, size=(1000, 1000))
   126                                         
   127     40.8 MiB      0.3 MiB           1       avg = arr1.mean()
   128     33.2 MiB     -7.6 MiB           1       del arr1
   129     33.2 MiB      0.0 MiB           1       return avg
   
Удаление объекта из памяти позволило увеличить ресурсы оперативной памяти
"""


# Example_3

# Проверим парсер на предмет расхода памяти

# class BaseExtractor:
#     @profile
#     def parse_list(self, array):
#         f = open('words.txt', 'w')
#         for word in array:
#             f.writelines(word)
#
#     @profile
#     def parse_url(self, url):
#         response = requests.get(url).text
#         with open('url.txt', 'w') as f:
#             f.writelines(response)

"""
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
   165     38.6 MiB     38.6 MiB           1       @profile
   166                                             def parse_url(self, url):
   167     50.5 MiB     11.8 MiB           1           response = requests.get(url).text
   168     50.5 MiB      0.0 MiB           1           with open('url.txt', 'w') as f:
   169                                                     # writing response to file
   170     50.5 MiB      0.0 MiB           1               f.writelines(response)


Filename: /home/nezl0i/sd/PYTHON/gb_algorithm/task_1.py

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
   159     45.8 MiB     45.8 MiB           1       @profile
   160                                             def parse_list(self, array):
   161     45.8 MiB      0.0 MiB           1           f = open('words.txt', 'w')
   162     45.8 MiB      0.0 MiB           6           for word in array:
   163     45.8 MiB      0.0 MiB           5               f.writelines(word)


Из результатов замера виден большой расход памяти в функции parse_url().
Оптимизируем функцию.

"""


class BaseExtractor:
    @profile
    def parse_list(self, array):
        f = open('words.txt', 'w')
        for word in array:
            f.writelines(word)

    @profile
    def parse_url(self, url):
        response = requests.get(url).text
        with open('url.txt', 'w') as f:
            f.writelines(response)
        del response

"""
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
   207     38.4 MiB     38.4 MiB           1       @profile
   208                                             def parse_url(self, url):
   209     50.2 MiB     11.8 MiB           1           response = requests.get(url).text
   210     50.2 MiB      0.0 MiB           1           with open('url.txt', 'w') as f:
   211                                                     # writing response to file
   212     50.2 MiB      0.0 MiB           1               f.writelines(response)
   213     45.6 MiB     -4.6 MiB           1           del response
   
Здесь мы видим, что память высвобождается, но только при завершении работы скрипта, т.е. применение в данной 
ситуации del не является оптимизацией, посколько garbage collector и так удалит объект из памяти по завершению 
работы скрипта. 
"""

if __name__ == '__main__':
    # main_func1()
    # main_func()
    # main_func2()

    url = 'https://raw.githubusercontent.com/dwyl/english-words/master/words.txt'
    array = ['one', 'two', 'three', 'four', 'five']
    extractor = BaseExtractor()
    extractor.parse_url(url)
    extractor.parse_list(array)

