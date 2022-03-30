# # Geek University Python-разработки - первая четверть - Основы языка Python.
# # Домашняя работа к уроку №6 задание 2
# * (вместо 1) Найти IP адрес спамера и количество отправленных им запросов по данным файла логов из предыдущего задания.
# Примечания: спамер — это клиент, отправивший больше всех запросов; код должен работать даже с файлами, размер которых превышает объем ОЗУ компьютера.

pars_list = []

with open('nginx_logs.txt', 'r') as f:
    for line in f:
        remote_addr_end = line.find('-', 0)
        remote_addr = line[0:remote_addr_end].replace(' ', '')

        request_type_start = line.find('"', 0)
        request_type_end = line.find('"', request_type_start+1)
        request_type = line[request_type_start:request_type_end].replace('"', '').split(' ')

        pars_list.append((remote_addr, request_type[0], request_type[1]))

check_spam = []
for x in pars_list:
    check_spam.append(x[0])

spamer = max(check_spam, key=check_spam.count)
count_spam = check_spam.count(spamer)

print(f'Спамер {spamer} спамил {count_spam} раз')
