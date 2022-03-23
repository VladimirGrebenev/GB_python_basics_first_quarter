# # Geek University Python-разработки - первая четверть - Основы языка Python.
# # Домашняя работа к уроку №5 задание 3
# Есть два списка:
# tutors = [
#     'Иван', 'Анастасия', 'Петр', 'Сергей',
#     'Дмитрий', 'Борис', 'Елена'
# ]
# klasses = [
#     '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
# ]
# Необходимо реализовать генератор, возвращающий кортежи вида (<tutor>, <klass>), например:
# ('Иван', '9А')
# ('Анастасия', '7В')
# ...
# Количество генерируемых кортежей не должно быть больше длины списка tutors. Если в списке klasses меньше элементов, чем в списке tutors, необходимо вывести последние кортежи в виде: (<tutor>, None), например:
# ('Станислав', None)
#
# ### Доказать, что вы создали именно генератор. Проверить его работу вплоть до истощения. Подумать, в каких ситуациях генератор даст эффект.

tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена',
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А'
]

def bagsha_list(list_1, list_2):
    if len(list_1) > len(list_2):
        for i in range(len(list_1)-len(list_2)):
            list_2.append(None)
    bagsha = list(zip(list_1, list_2))

    for item in bagsha:
        yield item

my_gen = bagsha_list(tutors, klasses)
print(type(my_gen))
print(my_gen)
print(next(my_gen), next(my_gen), next(my_gen))
print(next(my_gen), next(my_gen), next(my_gen))
print(next(my_gen))
print(next(my_gen))