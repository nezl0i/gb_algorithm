"""
Задание 3.

Для этой задачи:
1) придумайте 2-3 решения (не менее двух)
2) оцените сложность каждого решения в нотации О-большое
3) сделайте вывод, какое решение эффективнее и почему

Сама задача:
Имеется хранилище с информацией о компаниях: название и годовая прибыль.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.
Реализуйте поиск трех компаний с наибольшей годовой прибылью.
Выведите результат.

Примечание:
Без выполнения пунктов 2 и 3 задание считается нерешенным. Пункты 2 и 3 можно выполнить
через строки документации в самом коде.
Прошу вас внимательно читать ТЗ и не забыть выполнить все пункты.

Задание творческое. Здесь нет жестких требований к выполнению.
"""

##############################################################################
work_dict = {'Imperial': 27643, 'VoIP': 769012, 'NationalSystem': 109856, 'Lethal': 56009, 'IntKo': 91002,
             'Samsung': 90023498, 'MTC': 42023, 'TexnoPlast': 1907734}

##############################################################################
# example_1 Сложность O(n log n)


print(sorted(work_dict.items())[-3:])

##############################################################################
# example_2 Сложность O(n log n)


def ex_max_1(dict_default):
    v = sorted(list(dict_default.values()))
    return v[-3:]


print(ex_max_1(work_dict))

#############################################################################
# example_3 O(n^2)

total_list = []
for val in work_dict.values():
    total_list.append(val)
while len(total_list) != 3:
    total_list.remove(min(total_list))
for el in total_list:
    for key, val in work_dict.items():
        if el == val:
            print(key, ":", el)

