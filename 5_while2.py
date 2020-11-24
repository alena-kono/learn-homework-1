"""

Домашнее задание №1

Цикл while: ask_user со словарём

* Создайте словарь типа "вопрос": "ответ", например:
  {"Как дела": "Хорошо!", "Что делаешь?": "Программирую"} и так далее
* Напишите функцию ask_user() которая с помощью функции input()
  просит пользователя ввести вопрос, а затем, если вопрос есть
  в словаре, программа давала ему соотвествующий ответ. Например:

    Пользователь: Что делаешь?
    Программа: Программирую

"""

QUESTIONS_ANSWERS = {
    'how are you?': 'great',
    'what are you doing?': 'i am programming',
    'do you love python?': 'certainly yes',
    'could you make me a cup of tea?': 'maybe another time',
}


def ask_user(answers_dict: dict):

    while True:
        user_question = input('Ask me a question:\n').lower()
        print(answers_dict.get(
            user_question,
            'Sorry, I did not understand your question..'
            ))


if __name__ == "__main__":
    ask_user(answers_dict=QUESTIONS_ANSWERS)
