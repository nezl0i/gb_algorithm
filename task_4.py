"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции с каждым их них (заполнение, получение элемента) и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""

from collections import OrderedDict
from timeit import timeit
from random import randint

default_dict = {i: i for i in range(1000)}
default_orderdict = OrderedDict((i, i) for i in range(1000))

# 0.050699587000053725
print(timeit('{i: i for i in range(1000)}', globals=globals(), number=1000))

# 0.14100063299883914
print(timeit('OrderedDict((i, i) for i in range(1000))', globals=globals(), number=1000))

# 0.04673297899898898
print(timeit('default_dict.items()', globals=globals()))

# 0.04948997400060762
print(timeit('default_orderdict.items()', globals=globals()))

# 0.5907004059990868
print(timeit('default_dict.get(randint(0,100))', globals=globals()))

# 0.5894764469994698
print(timeit('default_orderdict.get(randint(0,100))', globals=globals()))

# 0.04789498399986769
print(timeit('default_dict.values()', globals=globals()))

# 0.04868922800051223
print(timeit('default_orderdict.values()', globals=globals()))

# В целом работа orderdict уступает по скорости обычному словарю. Тесты проводились на версии Python 3.9.5
# Использовать orderdict можно разве что для лаконичности написания кода, но его применение, как замена обычному словарю
# нецелесообразно.
