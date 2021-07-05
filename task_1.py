"""
Задание 1.
Реализуйте кодирование строки "по Хаффману".
У вас два пути:
1) тема идет тяжело? тогда вы можете, опираясь на пример с урока, сделать свою!!! версию алгоритма
Разрешается и приветствуется изменение имен переменных, выбор других коллекций, различные изменения
и оптимизации.

2) тема понятна? постарайтесь сделать свою реализацию.
Вы можете реализовать задачу, например, через ООП или предложить иной подход к решению.
"""
import queue


class Node:
    def __init__(self, freq, key=-1, left=None, right=None, code=''):
        self.freq = freq
        self.key = key
        self.left = left
        self.right = right
        self.code = code

    def __lt__(self, other):
        return self.freq < other.freq


def huffman_code(data_list):
    freq_table = {}
    node_list = []
    que = queue.PriorityQueue()
    code_table = {}

    for n in data_list:
        if n in freq_table:
            freq_table[n] += 1
        else:
            freq_table[n] = 1

    for k, v in freq_table.items():
        node_list.append(Node(v, k))
        que.put(node_list[-1])

    while que.qsize() > 1:
        n1 = que.get()
        n2 = que.get()
        n1.code = '1'
        n2.code = '0'
        nn = Node(n1.freq + n2.freq, left=n1, right=n2)
        node_list.append(nn)
        que.put(node_list[-1])

    def build_three(p, str_code=None):
        if str_code is None:
            str_code = []
        str_code.append(p.code)
        if p.left:
            build_three(p.left, str_code.copy())
            build_three(p.right, str_code.copy())
        else:
            code_table[p.key] = ''.join(str_code)

    build_three(node_list[-1])
    print(str(code_table))

    return code_table


if __name__ == '__main__':
    data = [1, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 4, 4, 5]
    huffman_code(data)
