# # Geek University Python-разработки - первая четверть - Основы языка Python.
# # Домашняя работа к уроку №3 задание 1
# Написать функцию num_translate(), переводящую числительные от 0 до 10 c
# английского на русский язык. Например:
# >>> num_translate("one")
# "один"
# >>> num_translate("eight")
# "восемь"
# Если перевод сделать невозможно, вернуть None. Подумайте, как
# и где лучше хранить информацию, необходимую для перевода:
# какой тип данных выбрать, в теле функции или снаружи.
# 2. * (вместо задачи 1) Доработать предыдущую функцию в num_translate_adv():
# реализовать корректную работу с числительными, начинающимися с заглавной буквы
# — результат тоже должен быть с заглавной. Например:
# >>> num_translate_adv("One")
# "Один"
# >>> num_translate_adv("two")
# "два"

def num_translate(en_word):
    """функция принимает числительные от 0 до 10 на EN и переводит их на RU"""
    trans_dict = {
        'one': 'один',
        'two': 'два',
        'three': 'три',
        'four': 'четыре',
        'five': 'пять',
        'six': 'шесть',
        'seven': 'семь',
        'eight': 'восемь',
        'nine': 'девять',
        'ten': 'десять',
    }

    if en_word.istitle():
        ru_word = trans_dict.get(en_word.lower()).title()
        return ru_word
    else:
        ru_word = trans_dict.get(en_word)
        return ru_word

print(num_translate('One'))
print(num_translate('eight'))
print(num_translate('twelve'))


