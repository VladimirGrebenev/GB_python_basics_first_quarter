# # Geek University Python-разработки - первая четверть - Основы языка Python.
# # Домашняя работа к уроку №7 задание 3
# Создать структуру файлов и папок, как написано в задании 2 (при помощи скрипта или «руками» в
# проводнике). Написать скрипт, который собирает все шаблоны в одну папку templates, например:
# |--my_project
#    ...
#   |--templates
#    |   |--mainapp
#    |   |  |--base.html
#    |   |  |--index.html
#    |   |--authapp
#    |      |--base.html
#    |      |--index.html
# Примечание: исходные файлы необходимо оставить; обратите внимание, что html-файлы расположены
# в родительских папках (они играют роль пространств имён); предусмотреть возможные исключительные
# ситуации; это реальная задача, которая решена, например, во фреймворке django.

import os
import shutil
import my_project

root_dir = my_project.__path__[0]
for root, dirs, files in os.walk(root_dir):
    if 'templates' in dirs:
        copy_path = os.path.join(root_dir, 'templates')
        t_file_path = os.path.join(root, 'templates')
        shutil.copytree(t_file_path, copy_path, dirs_exist_ok=True)