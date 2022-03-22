# # Geek University Python-разработки - первая четверть - Основы языка Python.
# # Домашняя работа к уроку №3 задание 4
# * (вместо задачи 3) Написать функцию thesaurus_adv(), принимающую в качестве
# аргументов строки в формате «Имя Фамилия» и возвращающую словарь, в котором
# ключи — первые буквы фамилий, а значения — словари, реализованные по схеме
# предыдущего задания и содержащие записи, в которых фамилия начинается с
# соответствующей буквы. Например:
# >>> thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья
# Иванов", "Анна Савельева")
# {
#     "А": {
#         "П": ["Петр Алексеев"]
#     },
#     "И": {
#         "И": ["Илья Иванов"]
#     },
#     "С": {
#         "И": ["Иван Сергеев", "Инна Серова"],
#         "А": ["Анна Савельева"]
#     }
# }

from pprint import pprint

def thesaurus_adv(*args):
    """принимает имена, возвращает словарь типа {'А': {'П': ['Петр Алексеев']}"""
    name_dict = {} # словарь с ключами по Фамилии
    for el in args:
        key_1 = el.split(' ')[1][0] # буква Фамилии
        # заполняем словарь с ключами по Фамилии
        name_dict[key_1] = (list(filter(lambda n: n.split(' ')[1][0].startswith(key_1), args)))

    # перебираем словарь с ключами по Фамилии для замены значений подсловарями
    for key, value in name_dict.items():
        sub_dict = {} # пoдcлoвapь с ключом по букве Имени
        for el in value: #перебор значений списка по именам
            key_2 = el.split(' ')[0][0] # буква Имени
            #создание списка отфильтрованного по букве Имени
            #создание словаря с ключём по букве Имени и значением списка имён по букве Имени
            sub_dict[key_2] = (list(filter(lambda n: n.split(' ')[0][0].startswith(key_2), value)))
        name_dict[key] = sub_dict

    return name_dict

#сортировка по ключам - параметр sort_dicts=True установлен по умолчанию в pprint
pprint(thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев",
                     "Илья Иванов", "Анна Савельева"))