"""
Задание 3.
Определить количество различных (уникальных) подстрок с использованием хеш-функции.
Дана строка S длиной N, состоящая только из строчных латинских букв.

Подсказка: примените вычисление хешей для подстрок с помощью хеш-функций и множества
Можно воспользоваться ф-цией hash() (см. материалы к уроку)

Пример:
рара - 6 уникальных подстрок

рар
ра
ар
ара
р
а
"""

from hashlib import sha256


def get_str_hash(str_text):
    element = set()
    for i in range(1, len(str_text)):
        for j in range(len(str_text)):
            block = str_text[j: j + i]
            element.add(block)
            print(sha256(block.encode('utf-8')).hexdigest())
    return element


print(get_str_hash('papa'))


