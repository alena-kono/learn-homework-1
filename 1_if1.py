"""

Домашнее задание №1

Условный оператор: Возраст

* Попросить пользователя ввести возраст при помощи input и положить
  результат в переменную
* Написать функцию, которая по возрасту определит, чем должен заниматься пользователь:
  учиться в детском саду, школе, ВУЗе или работать
* Вызвать функцию, передав ей возраст пользователя и положить результат
  работы функции в переменную
* Вывести содержимое переменной на экран

"""

def main():

    def determine_user_status(age):
        try:
            age = int(age)
        except ValueError:
            return 'Incorrect input'

        if age < 0:
            return f'You have not been born yet..'
        elif 1 <= age <= 3:
            return f'You should be with mom at home at the age of {age}'
        elif 4 <= age <= 6:
            return f'You should go to kindergarden at the age of {age}'
        elif 7 <= age <= 18:
            return f'You should study at school at the age of {age}'
        elif 19 <= age <= 22:
            return f'You should study at university at the age of {age}'
        elif age >= 75:
            return f'You should retire at the age of {age}'
        else:
            return f'Sorry, but You should work at the age of {age}'


    user_age = input('Please, enter your age (integer number): ')
    current_user_status = determine_user_status(age=user_age)
    print(current_user_status)


if __name__ == "__main__":
    main()
