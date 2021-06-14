"""
Задание 4.

Для этой задачи:
1) придумайте 2-3 решения (не менее двух)
2) оцените сложность каждого решения в нотации О-большое
3) сделайте вывод, какое решение эффективнее и почему

Сама задача:
Пользователи веб-ресурса проходят аутентификацию.
В системе хранятся логин, пароль и отметка об активации учетной записи.

Нужно реализовать проверку, может ли пользователь быть допущен к ресурсу.
При этом его учетка должна быть активирована.
А если нет, то польз-лю нужно предложить ее пройти.

Приложение должно давать ответы на эти вопросы и быть реализовано в виде функции.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.

Примечание:
Без выполнения пунктов 2 и 3 задание считается нерешенным. Пункты 2 и 3 можно выполнить
через строки документации в самом коде.
Прошу вас внимательно читать ТЗ и не забыть выполнить все пункты.

Задание творческое. Здесь нет жестких требований к выполнению.
"""

################################################################################
auth_bd = {'login': 'CoolUser', 'password': 'vbQ34uuM7', 'active': True}
list_answer = ['yes', 'Yes', 'y', 'Y', 'да', 'Да']

################################################################################
# Example_1 O(n^2)


def web_auth(login, passwd):
    if login and passwd in auth_bd.values():
        if auth_bd.get('active'):
            print('Authorization was successful!')
        else:
            answer = input('Account is not activated. Activate? ')
            if answer in list_answer:
                auth_bd['active'] = True
                print('Account activated!')
            else:
                print('Buy!!')
    else:
        print('User not registered.')
    return

################################################################################
# Example_2 Сложность O(n)


def check_active():
    if auth_bd['active']:
        print('Authorization was successful!')
        return
    else:
        print('Account is not activated. Activate? ')
        print('Account activated!') if input() in list_answer else print('Buy')
    return


def check_auth(login, passwd):
    check_login = True if auth_bd['login'] == login else False
    check_passwd = True if auth_bd['password'] == passwd else False
    if check_login and check_passwd:
        check_active()
    return


if __name__ == '__main__':
    user_login = input('User login: ')
    user_password = input('Password : ')
    # web_auth(user_login, user_password)
    check_auth(user_login, user_password)
