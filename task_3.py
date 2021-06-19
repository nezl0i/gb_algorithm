"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через cProfile и через timeit

Обязательно предложите еще свой вариант решения и также запрофилируйте!

Сделайте вывод, какая из четырех реализаций эффективнее и почему!!!

Без аналитики задание считается не принятым
"""
from timeit import timeit


def revers_1(enter_num, revers_num=0):
    if enter_num == 0:
        return revers_num
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        return revers_1(enter_num, revers_num)


def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num


def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num


def revers_4(enter_num):
    revers_num = ''.join(reversed(str(enter_num)))
    return revers_num


n = 9025893636

print(timeit("revers_1(n)", globals=globals(), number=100000))
print(timeit("revers_2(n)", globals=globals(), number=100000))
print(timeit("revers_3(n)", globals=globals(), number=100000))
print(timeit("revers_4(n)", globals=globals(), number=100000))


# revers_1 (0.2423238) Самый медленный, поскольку используется рекурсия
# revers_2 (0.1836739) Более быстрый способ с применением цикла
# revers_3 (0.031263200000000047) Самый быстрый вариант, поскольку используем срез. Сложность О(1).
# revers_4 (0.06472639999999996) Вариант оптимальный и лаконичный. По скорости тоже.
