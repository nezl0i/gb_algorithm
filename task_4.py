"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносить ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования и хеш-таблиц
Можете условжнить задачу, реализовав ее через ООП
Не забудьте, что кэширование - механизм, а хеш-таблица - средство его реализации.

Задание творческое. Здесь нет жестких требований к выполнению.
"""

from hashlib import sha256

SALT = 'hT56+@#hy7--'
DICT_URL = {}


def get_hash(url):
    if DICT_URL.get(url):
        print(f'{url} есть в кеше')
    else:
        hash_url = sha256(SALT.encode('utf-8') + url.encode('utf-8')).hexdigest()
        DICT_URL[url] = hash_url
        print(f'Страница {url} добавлена в хеш')


get_hash('https://www.yandex.ru/')
get_hash('https://www.yandex.ru/')
get_hash('https://www.google.com/')
get_hash('https://www.google.com/')
