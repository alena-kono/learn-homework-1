"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию hello_user() из задания while1, чтобы она
  перехватывала KeyboardInterrupt, писала пользователю "Пока!"
  и завершала работу при помощи оператора break

"""


def hello_user():

    user_answer = ''

    while user_answer != 'Fine':
        try:
            user_answer = input('How are you?\n')
        except KeyboardInterrupt:
            print('', 'Bye!', sep=' ')
            break


if __name__ == "__main__":
    hello_user()
