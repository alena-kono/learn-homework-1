"""

Домашнее задание №1

Цикл while: hello_user

* Напишите функцию hello_user(), которая с помощью функции input() спрашивает
  пользователя “Как дела?”, пока он не ответит “Хорошо”

"""


def hello_user():

  user_answer = ''

  while user_answer != 'Fine':
      user_answer = input('How are you?\n')



if __name__ == "__main__":
    hello_user()
