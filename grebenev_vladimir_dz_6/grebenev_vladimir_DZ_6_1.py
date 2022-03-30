# # Geek University Python-разработки - первая четверть - Основы языка Python.
# # Домашняя работа к уроку №6 задание 1
# 1. Не используя библиотеки для парсинга, распарсить (получить определённые данные) файл логов web-сервера nginx_logs.txt
# (https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs) — получить список кортежей вида: (<remote_addr>, <request_type>, <requested_resource>). Например:
#
# [
# ...
# ('141.138.90.60', 'GET', '/downloads/product_2'),
# ('141.138.90.60', 'GET', '/downloads/product_2'),
# ('173.255.199.22', 'GET', '/downloads/product_2'),
# ...
# ]
#
# Примечание: код должен работать даже с файлами, размер которых превышает объем ОЗУ компьютера.
from pprint import pprint

pars_list = []

with open('nginx_logs.txt', 'r') as f:
    for line in f:
        remote_addr_end = line.find('-', 0)
        remote_addr = line[0:remote_addr_end].replace(' ', '')

        request_type_start = line.find('"', 0)
        request_type_end = line.find('"', request_type_start+1)
        request_type = line[request_type_start:request_type_end].replace('"', '').split(' ')

        pars_list.append((remote_addr, request_type[0], request_type[1]))

pprint(pars_list)