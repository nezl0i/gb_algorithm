"""
Задание 1.

Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива

Сделайте замеры времени выполнения кода с помощью модуля timeit

Оптимизируйте, чтобы снизить время выполнения
Проведите повторные замеры.

Добавьте аналитику: что вы сделали и почему!!!
Без аналитики задание не принимается
"""
from timeit import timeit


# Цикл for
def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


# Генератор списка
def func_3(nums):
    new_arr = (el for ind, el in enumerate(nums) if not ind % 2)
    return new_arr


# Применение filter
def func_4(nums):
    return filter(lambda i: nums[i] % 2 == 0, range(len(nums)))


default_list = [i for i in range(50)]

print(timeit("func_1(default_list)", globals=globals(), number=150000))  # 0.6585903
print(timeit("func_3(default_list)", globals=globals(), number=150000))  # 0.0596662
print(timeit("func_4(default_list)", globals=globals(), number=150000))  # 0.05944329999999998


# По проведенным замерам видно, что применение встроенной функции filter
# значительно ускоряет работу программы. func_1 работает дольше, поскольку
# в ней спользуется цикл for. Генератор списка также работает достаточно быстро.

