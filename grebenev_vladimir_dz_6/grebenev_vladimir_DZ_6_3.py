# # Geek University Python-разработки - первая четверть - Основы языка Python.
# # Домашняя работа к уроку №6 задание 3
# Есть два файла: в одном хранятся ФИО пользователей сайта, а в другом — данные об их хобби.
# Известно, что при хранении данных используется принцип: одна строка — один пользователь,
# разделитель между значениями — запятая. Написать код, загружающий данные из обоих файлов
# и формирующий из них словарь: ключи — ФИО, значения — данные о хобби. Сохранить словарь в файл.
# Проверить сохранённые данные. Если в файле, хранящем данные о хобби, меньше записей, чем в файле
# с ФИО, задаём в словаре значение None. Если наоборот — выходим из скрипта с кодом «1».
# При решении задачи считать, что объём данных в файлах во много раз меньше объема ОЗУ.
# Фрагмент файла с данными о пользователях (users.csv):
# Иванов,Иван,Иванович
# Петров,Петр,Петрович
# Фрагмент файла с данными о хобби (hobby.csv):
# скалолазание,охота
# горные лыжи
users = []
with open('site_users.csv', encoding='utf-8') as f_users:
    for line in f_users:
        users.append(line.replace(',', ' ').replace('\n', ''))

hobby = []
with open('users_hobby.csv', encoding='utf-8') as f_hobby:
    for line in f_hobby:
        hobby.append(line.replace('\n', ''))

if len(hobby) < len(users):
    while len(hobby) < len(users):
        hobby.append(None)
    hobby_dict = dict(zip(users, hobby))
elif len(hobby) == len(users):
    hobby_dict = dict(zip(users, hobby))
else:
    quit(1)

with open('hobby_dict.txt', 'w', encoding='utf-8') as f_dict:
    for key, value in hobby_dict.items():
        f_dict.writelines(f'{key}: {value} \n')
