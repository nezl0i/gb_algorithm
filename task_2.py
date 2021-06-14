"""
Задание 2.

Реализуйте два алгоритма.

Первый, в виде функции, должен обеспечивать поиск минимального значения для списка.
В основе алгоритма должно быть сравнение каждого числа со всеми другими элементами списка.
Сложность такого алгоритма: O(n^2) - квадратичная.

Второй, в виде функции, должен обеспечивать поиск минимального значения для списка.
Сложность такого алгоритма: O(n) - линейная.

Не забудьте указать сложность каждого из двух алгоритмов. Для лучшего закрепления темы
можете определить и указать сложность еще и у каждого выражения этих двух алгоритмов.

Примечание:
Прошу вас внимательно читать ТЗ и не забыть выполнить все пункты.
"""

####################################################################
# example_1 Сложность О(n^2)


def min_check2(default_list):
    for i in range(len(default_list) - 1):  # O(n)
        min_digit = default_list[i]  # O(1)
        for j in default_list:       # O(n)
            if j < min_digit:        # O(1)
                min_digit = j        # O(1)
        return min_digit             # O(1)

####################################################################
# example_2 Сложность О(n)


def min_check(default_list):
    min_digit = default_list[0]  # O(1)
    for el in default_list:  # O(n)
        if el < min_digit:  # O(1)
            min_digit = el  # O(1)
    return min_digit  # O(1)


u_list = [9, 8, 12, 56, 4, 9, 2]

print(min_check2(u_list))
