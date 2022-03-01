# # Geek University Python-разработки - первая четверть - Основы языка Python.
# # Домашняя работа к уроку №3 задание 5
# Реализовать функцию get_jokes(), возвращающую n шуток,
# сформированных из трех случайных слов, взятых из трёх списков
# (по одному из каждого):
# nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
# adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
# adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
#         Например:
# >>> get_jokes(2)
# ["лес завтра зеленый", "город вчера веселый"]
# Документировать код функции.
# Сможете ли вы добавить еще один аргумент — флаг, разрешающий
# или запрещающий повторы слов в шутках (когда каждое слово можно использовать
# только в одной шутке)? Сможете ли вы сделать аргументы именованными?
from random import choice

def get_jokes(number = 1, switch = True):
    """функция возвращает number шуток, switch = True разрешает
    повтор строк"""

    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

    if switch == True:
        for i in range(number):
            print(f'{choice(nouns)} {choice(adverbs)} {choice(adjectives)}')
    else:
        if number > len(nouns):
            print(f'я не могу создать больше {len(nouns)} шуток с '
                  f'неповторяемыми словами')
        else:
            for i in range(number):
                first_word = choice(nouns)
                nouns.remove(first_word)
                second_word = choice(adverbs)
                adverbs.remove(second_word)
                third_word = choice(adjectives)
                adjectives.remove(third_word)
                print(f'{first_word} {second_word} {third_word}')

get_jokes(number=5, switch=False)
# get_jokes(number=3, switch=True)
# get_jokes(number=10, switch=True)
# get_jokes(number=10, switch=False)
