"""
Задание 2.
Ваша программа должна запрашивать пароль
Для этого пароля вам нужно получить хеш, используя функцию sha256
Для генерации хеша обязательно нужно использовать криптографическую соль
Обязательно выведите созданный хеш.

Далее программа должна запросить пароль повторно
Вам нужно проверить, совпадает ли пароль с исходным
Для проверки необходимо сравнить хеши паролей

ПРИМЕР:
Введите пароль: 123
В базе данных хранится строка: 555a3581d37993843efd4eba1921f1dcaeeafeb855965535d77c55782349444b
Введите пароль еще раз для проверки: 123
Вы ввели правильный пароль

Обязательно усложните задачу! Добавьте сохранение хеша в файле и получение его из файла.
А если вы знаете как через Python работать с БД, привяжите к заданию БД и сохраняйте хеши там.
"""
import sqlite3
from hashlib import sha256


class Base:
    def __init__(self, db):
        self.conn = sqlite3.connect(db, check_same_thread=False)
        self.cur = self.conn.cursor()

    def query(self, arg, tuples=''):
        self.cur.execute(arg, tuples)
        self.conn.commit()
        return self.cur

    def stat(self):
        self.conn.commit()

    def __del__(self):
        self.conn.close()


bd = Base('users.db')


def check_passwd():
    input_ = input('Enter password: ')

    salt = '3459*99%6ghdA'
    hashed_password = sha256(input_.encode('utf-8') + salt.encode('utf-8')).hexdigest()
    # print(hashed_password)

    sql = f'SELECT password, user FROM "user" WHERE ("password" ' \
          f'LIKE "%{hashed_password}%");'
    result = bd.query(sql).fetchall()
    if len(result) != 0:
        return 'Your Password is correct!!!'
    else:
        sqlite_insert = f'INSERT INTO user ' \
                        f'(password, user) ' \
                        f'VALUES {hashed_password, input_};'
        bd.query(sqlite_insert)
        bd.stat()
        print('Password insert in DataBase.')
        return check_passwd()


if __name__ == '__main__':
    print(check_passwd())
