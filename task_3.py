"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на
две равные по длине части: в одной находятся элементы, которые не меньше медианы,
в другой – не больше медианы.

Задачу можно решить без сортировки исходного массива.

Но если это слишком сложно, то используйте метод сортировки,
который не рассматривался на уроках: Шелла, Гномья, Кучей...
https://github.com/nezl0i/gb_algorithm/pull/7
"""
import random
from statistics import median
from timeit import timeit


def select_depths(count, array):
    pivot = random.choice(array)

    lesser = [item for item in array if item < pivot]
    if len(lesser) > count:
        return select_depths(count, lesser)
    count -= len(lesser)
    num_equal = array.count(pivot)
    if num_equal > count:
        return pivot
    count -= num_equal

    sample_list = [item for item in array if item > pivot]
    return select_depths(count, sample_list)


def search_median(array):
    if len(array) % 2:
        return select_depths(len(array)//2, array)
    else:
        left = select_depths((len(array)-1) // 2, array)
        right = select_depths((len(array)+1) // 2, array)
        return (left + right) / 2


if __name__ == '__main__':
    m = int(input('Введите m для исходного массива: '))
    default_array = [random.randint(0, 100) for _ in range(2*m + 1)]
    print(f'Исходный массив: {default_array}')
    print(f'Медиана: {search_median(default_array[:])}')
    print('Время поиска медианы -',
          timeit("search_median(default_array[:])", globals=globals(), number=1500))  # 0.012961838001501746
    print(f'Медиана (statistics.median): {median(default_array[:])}')
    print('Время поиска медианы (statistics.median) -',
          timeit("median(default_array[:])", globals=globals(), number=1500))  # 0.001084626986994408

    # Поиск медианы отличный от встроенного метода проигрывает в скорости из-за сложности подхода.
