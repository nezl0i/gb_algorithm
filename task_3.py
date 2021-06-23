"""
Задача 3.
В соответствии с документацией Python,
deque – это обобщение стеков и очередей.
Вот основное правило: если вам нужно что-то быстро дописать или вытащить, используйте deque.
Если вам нужен быстрый случайный доступ, используйте list.

Задача: 
1) создайте простой список (list) и очередь (deque). Сделайте замеры и оцените что заполняется быстрее.
2) Выполните различные операции с каждым из объектов. Сделайте замеры и оцените, где и какие операции быстрее.

Не забудьте, что сравнивать, например, можно операцию appendleft дека и insert списка и т.д.
"""
from collections import deque
from timeit import timeit
from random import randint

default_list = [i for i in range(1000)]
default_deque = deque([i for i in range(1000)])

# 0.050834218000090914
print('Append =list=', timeit('default_list.append(10)', globals=globals()))

# 0.04547909999928379
print('Append =deque=', timeit('default_deque.append(10)', globals=globals()))

# 6.807905509000193
print('Insert =list=', timeit('default_list.insert(0,10)', globals=globals(), number=10000))

# 0.000494427000376163
print('Appendleft =deque=', timeit('default_deque.appendleft(10)', globals=globals(), number=10000))

# 0.04136672200002067
print('Pop =list=', timeit('default_list.pop()', globals=globals()))

# 0.03919533800035424
print('Pop =deque=', timeit('default_deque.pop()', globals=globals()))

# 0.010537304000536096
print('Pop(i) =list=', timeit('default_list.pop(0)', globals=globals(), number=10000))

# 0.0004128990003664512
print('Popleft =deque=', timeit('default_deque.popleft()', globals=globals(), number=10000))

# 0.059423799999422044
print('Random =list=', timeit('default_list[randint(0, 500)]', globals=globals(), number=100000))

# 0.062008692999370396
print('Random =deque=',
      timeit('default_deque[randint(0, 500)]', globals=globals(), number=100000))

# Deque работает быстрее списка, это очевидно. Единственное, проигрывает незначительно в выборе эелементов списка по
# его индексу. Сделанные замеры показывают приоритетные операции Deque.
