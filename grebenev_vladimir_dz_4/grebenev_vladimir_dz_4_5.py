# # Geek University Python-разработки - первая четверть - Основы языка Python.
# # Домашняя работа к уроку №4 задание 4

from utils import currency_rates
from pprint import pprint
from sys import argv

pprint(currency_rates(*argv[1:]))



