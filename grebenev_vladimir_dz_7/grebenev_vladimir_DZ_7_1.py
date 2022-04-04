# # Geek University Python-разработки - первая четверть - Основы языка Python.
# # Домашняя работа к уроку №7 задание 1
# Написать скрипт, создающий стартер (заготовку) для проекта со следующей структурой папок:
# |--my_project
#    |--settings
#    |--mainapp
#    |--adminapp
#    |--authapp
# Примечание: подумайте о ситуации, когда некоторые папки уже есть на диске (как быть?); как лучше
# хранить конфигурацию этого стартера, чтобы в будущем можно было менять имена папок под конкретный
# проект; можно ли будет при этом расширять конфигурацию и хранить данные о вложенных папках и файлах
# (добавлять детали)?
import os

def make_stracture(main_dir = 'my_project', dirs = ['settings', 'mainapp', 'adminapp','authapp']):
    if not os.path.exists(main_dir):
        os.mkdir(main_dir)
    for dir in dirs:
        dir_path = os.path.join(main_dir, dir)
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)

make_stracture()
