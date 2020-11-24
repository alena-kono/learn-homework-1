"""

Домашнее задание №1

Цикл for: Оценки

* Создать список из словарей с оценками учеников разных классов
  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе.
* Посчитать и вывести средний балл по каждому классу.
"""

def main():

    SCORES_JOURNAL = [
    {'school_class': '1a', 'scores': [2, 5, 5, 4, 3]},
    {'school_class': '1b', 'scores': [3, 4, 4, 4.5, 3]},
    {'school_class': '2a', 'scores': [1, 5, 5, 5, 5]},
    {'school_class': '2c', 'scores': [4, 4, 2, 3]},
    {'school_class': '3a', 'scores': [2, 5]},
    {'school_class': '3d', 'scores': [2, 5, 5, 4, 3, 4, 4, 3, 2]}
    ]

    total_score_per_school = 0
    scores_count_per_school = 0

    for grade in SCORES_JOURNAL:
        for score in grade['scores']:
            total_score_per_school += score
            scores_count_per_school += 1

    print(f'Average score for this school is \
{round(total_score_per_school / scores_count_per_school, 3)}')

    total_score_per_grade = 0

    for grade in SCORES_JOURNAL:
        avrg_score_per_grade = round(
            sum(grade['scores']) / len(grade['scores']), 2)

        print(f'Average score for {grade["school_class"]} \
is {avrg_score_per_grade}')


if __name__ == "__main__":
    main()
