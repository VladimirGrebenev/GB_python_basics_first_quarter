# # Geek University Python-разработки - первая четверть - Основы языка Python.
# # Домашняя работа к уроку №8 задание 1
# Написать функцию email_parse(<email_address>), которая при помощи регулярного выражения извлекает
# имя пользователя и почтовый домен из email адреса и возвращает их в виде словаря. Если адрес
# не валиден, выбросить исключение ValueError. Пример:
# >>> email_parse('someone@geekbrains.ru')
# {'username': 'someone', 'domain': 'geekbrains.ru'}
# >>> email_parse('someone@geekbrainsru')
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   ...
#     raise ValueError(msg)
# ValueError: wrong email: someone@geekbrainsru
# Примечание: подумайте о возможных ошибках в адресе и постарайтесь учесть их в регулярном выражении;
# имеет ли смысл в данном случае использовать функцию re.compile()?
import re
my_notebook = []
def email_parse(email_address_list):
    """принимает список email, проверяет их валидность и возвращает ({name:domain})"""
    RE_EMAIL = re.compile(r'\b[\w\._+-]+@[\w\._+-]+\.[a-z]{2,3}\b')

    for email in email_address_list:
        assert RE_EMAIL.match(email), f'wrong email: {email}'

        username = email.split('@', maxsplit = 1)[0]
        domain = email.split('@', maxsplit = 1)[1]
        my_notebook.append({'username': username, 'domain': domain})

    return my_notebook

my_email = ('grebenev-81@mail.ru', 'g_e+e_k@look.com',)
print(email_parse(my_email))