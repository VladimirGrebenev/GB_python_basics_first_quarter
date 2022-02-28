# Geek University Python-разработки - первая четверть - Основы языка Python.
# Домашняя работа к уроку №2 задание 4
#  Дан список, содержащий искажённые данные с должностями и именами сотрудников:
# ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА',
#  'токарь высшего разряда нИКОЛАй', 'директор аэлита']

error_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА',
              'токарь высшего разряда нИКОЛАй', 'директор аэлита']
print(error_list, '\n', id(error_list))

# не изменяя список
# for i in range(len(error_list)):
#     print(f'Привет, {error_list[i].split()[-1].title()}!')
#     print(f'Привет, {error_list[i].split().pop().title()}!')

# for el in error_list:
#     print(f'Привет, '
#           f'{el.replace(el.split()[-1], el.split()[-1].title()).split().pop()}!')

# изменяя список
for index, item in enumerate(error_list):
    error_list[index] = error_list[index].replace(item.split()[-1],
                                                  item.split()[-1].title())
    print(f'Привет, {error_list[index].split().pop()}!')

print(error_list, '\n', id(error_list))