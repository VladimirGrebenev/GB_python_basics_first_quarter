# # Geek University Python-разработки - первая четверть - Основы языка Python.
# # Домашняя работа к уроку №4 задание 2
# Написать функцию currency_rates(), принимающую в качестве аргумента код валюты
# (например, USD, EUR, GBP, ...) и возвращающую курс этой валюты по отношению
# к рублю. Использовать библиотеку requests. В качестве API можно использовать
# http://www.cbr.ru/scripts/XML_daily.asp. Рекомендация: выполнить предварительно
# запрос к API в обычном браузере, посмотреть содержимое ответа. Можно ли, используя
# только методы класса str, решить поставленную задачу? Функция должна возвращать
# результат числового типа, например float. Подумайте: есть ли смысл для работы
# с денежными величинами использовать вместо float тип Decimal? Сильно ли усложняется
# код функции при этом? Если в качестве аргумента передали код валюты, которого
# нет в ответе, вернуть None. Можно ли сделать работу функции не зависящей от того,
# в каком регистре был передан аргумент? В качестве примера выведите курсы доллара
# и евро.
# # Домашняя работа к уроку №4 задание 2
# * (вместо 2) Доработать функцию currency_rates(): теперь она должна возвращать кроме курса
# дату, которая передаётся в ответе сервера. Дата должна быть в виде объекта date. Подумайте,
# как извлечь дату из ответа, какой тип данных лучше использовать в ответе функции?
import requests
from pprint import pprint

def currency_rates(*args):
    """принимает коды валют (например 'USD', 'EUR', 'GBP', ...) и возвращает их курсы к рублю"""

    exchange_rate = []
    response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    cur_date = response.headers['Date']
    page = response.text
    for currency in args:
        currency = str(currency)
        currency = currency.upper()
        try:
            index_cur = page.index(currency) #индекс первого символа валюты в строке страницы
            index_val = page.find('</Value>', index_cur)
            cur_value = float(page[index_val-7: index_val].replace(',', '.'))
        except:
            cur_value = None
        rezult = f'Курс {currency} на {cur_date} равен {cur_value} RUB'
        exchange_rate.append(rezult)

    return exchange_rate

if __name__ == '__main__':
    pprint(currency_rates('usd', 'eUr', 'Val' ))