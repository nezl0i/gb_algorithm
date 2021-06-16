"""
Задание 1.

Реализуйте свои пользовательские функции, в которых реализуйте:

a) заполнение списка и словаря,
   сделайте замеры и сделайте выводы, что выполняется быстрее и почему
b) выполните набор операций и со списком, и со словарем,
   сделайте замеры и сделайте выводы, что и где выполняется быстрее и почему

Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)

Примечание: если вы уже знаете, что такое декоратор и как его реализовать,
то реализуйте ф-цию-декоратор для подсчета времени работы ваших пользовательских функций
И примените ее к своим функциям!

Прошу вас внимательно читать ТЗ и не забыть выполнить все пункты.
"""
import time


# Функция декоратор
def timing(func):
    def time_code(*arg, **kwarg):
        t_start = time.time() * 1000
        result = func(*arg, **kwarg)
        t_stop = time.time() * 1000
        return f'Time - {(t_stop - t_start)}', result, func.__name__
    return time_code


# Заполнение списка в цикле
@timing
def create_list_1(n):
    default_list = []
    for i in range(n):
        default_list.append(i)
    return default_list


# Заполнение списка, применяя генератор
@timing
def create_list_2(n):
    default_list = [i for i in range(n)]
    return default_list


# Генерация вложенных списков
@timing
def create_list_3():
    default_list = [[i * j for i in range(0, 3)] for j in range(0, 3)]
    return default_list


# Генератор списка с lambda
@timing
def create_list_4():
    default_list = [(lambda i: i*i)(i) for i in range(0, 20)]
    return default_list


print(create_list_1(20))
print(create_list_2(20))
print(create_list_3())
print(create_list_4())

"""
Возможности, представленные генераторами списков 
позволяют повысить скорость и эффективность обработки данных
"""


# Создание словаря
@timing
def create_dict_1():
    default_dict = {'dict': 1, 'dictionary': 2}
    return default_dict


# Создание словаря с помощью функции dict
@timing
def create_dict_2():
    default_dict = dict(short='dict', long='dictionary')
    return default_dict


# Создание словаря с помощью метода fromkeys
@timing
def create_dict_3():
    default_dict = dict.fromkeys(['a', 'b'], 100)
    return default_dict


# Создание словаря с помощью генераторов словарей
@timing
def create_dict_4():
    default_dict = {a: a ** 2 for a in range(10)}
    return default_dict


print(create_dict_1())
print(create_dict_2())
print(create_dict_3())
print(create_dict_4())


"""
Создание словарей с применением встроенных функций, таких как fromkeys
ускоряет работу приложения.
"""

