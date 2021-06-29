"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный
и отсортированный массивы.

Хотя в примерах к уроку уже есть вариант реализации слияния,
попробуйте предложить другой (придумать или найти).

И попытаться сделать замеры на массивах разной длины: 10, 100, 1000, ...

Пример:
Введите число элементов: 5
Исходный - [46.11436617832828, 41.62921998361278, 18.45859540989644, 12.128870723745806, 8.025098788570562]
Отсортированный - [8.025098788570562, 12.128870723745806, 18.45859540989644, 41.62921998361278, 46.11436617832828]
"""
import operator
import random
from timeit import timeit


def merge(left, right, compare):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if compare(left[i], right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result


def mergeSort(array, compare=operator.lt):
    if len(array) < 2:
        return array[:]
    else:
        middle = len(array) // 2
        left = mergeSort(array[:middle], compare)
        right = mergeSort(array[middle:], compare)
        return merge(left, right, compare)


if __name__ == '__main__':
    count = int(input('Введите количество элементов массива: '))
    default_list = []
    for i in range(count):
        default_list.append(random.uniform(0, 51))
    print('Исходный массив:', default_list)

    print('Время сортировки массива -',
          timeit("mergeSort(default_list[:], compare=operator.lt)", globals=globals(), number=1500))
    print('Отсортированный массив:', mergeSort(default_list, compare=operator.lt))

# Время сортировки массива из 10 элементов - 0.023770987005264033
# Время сортировки массива из 100 элементов - 0.27851654299593065
# Время сортировки массива из 1000 элементов - 3.664885079000669
# Увеличение времени происходит пропорционально увеличению элементов в исходном массиве
