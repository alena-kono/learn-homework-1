"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками.
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры
  и выводя на экран результаты

"""

def main():

    def compare_strings(first_str, second_str, predefined_str='learn'):
        if not isinstance(
            first_str, str
            ) or not isinstance(
                second_str, str
                ):
            return 0
        elif first_str == second_str:
            return 1
        elif len(first_str) > len(second_str):
            return 2
        elif second_str == predefined_str:
            return 3
        else:
            return f'This function is not designed to handle such input values'


    SOME_VALUES = [
        (1, 'sample'),
        (34, 100),
        ('test', 'test'),
        ('long-long-string', 'same test'),
        ('learn', '1.45'),
        ('short', 'LONGLONGLONG'),
        ('e', 'learnpython'),
        ('learn', 'learn'),
    ]

    for pair in SOME_VALUES:
        one, two = pair
        print(f'Input data: {pair}\nResult: {compare_strings(one, two)}')
        print('*' * 70)


if __name__ == "__main__":
    main()
