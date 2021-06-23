"""
2. Написать программу сложения и умножения двух шестнадцатиричных чисел.
При этом каждое число представляется как массив, элементы которого это цифры числа.
Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

Подсказка:
Для решения задачи обязательно примените какую-нибудь коллекцию из модуля collections
Для лучшее освоения материала можете даже сделать несколько решений этого задания,
применив несколько коллекций из модуля collections
Также попробуйте решить задачу вообще без collections и применить только ваши знания по ООП
(в частности по перегрузке методов)

__mul__
__add__

Пример:
Например, пользователь ввёл A2 и C4F.
Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’]
Произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

1. вариант
defaultdict(list)
int(, 16)
reduce

2. вариант
class HexNumber:
    __add__
    __mul__

hx = HexNumber
hx + hx
hex()
"""

# Example 1

from collections import defaultdict


def hex_calc():
    numbers = defaultdict(list)
    for i in range(2):
        numbers[f'{i}'] = list(input(f'Введите {i + 1} число  в формате HEX: '))

    addition = 0
    multiplication = 1
    for val in numbers.values():
        addition += int(''.join(val), 16)
        multiplication *= int(''.join(val), 16)
    print(f'Сумма - {list(hex(addition))[2:]}')
    print(f'Произведение - {list(hex(multiplication))[2:]}')


hex_calc()

# Example 2


class HexCalc:

    def __init__(self, hex_digit):
        self.hex_digit = hex_digit

    def __str__(self):
        return f'{self.hex_digit}'

    def __add__(self, other):
        try:
            return hex(int(self.hex_digit, 16) + int(other.hex_digit, 16)).upper()[2:]
        except ValueError:
            print("Неверный формат числа")

    def __mul__(self, other):
        try:
            return hex(int(self.hex_digit, 16) * int(other.hex_digit, 16)).upper()[2:]
        except ValueError:
            print("Неверный формат числа")


one_hex = HexCalc(input('Введите первое число в формате HEX: '))
two_hex = HexCalc(input('Введите второе число в формате HEX: '))
print('Сумма -', one_hex + two_hex)
print('Произведение', one_hex * two_hex)
