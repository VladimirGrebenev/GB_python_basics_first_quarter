# Geek University Python-разработки - первая четверть - Основы языка Python.
# Домашняя работа к уроку №2 задание 2
# ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
# Необходимо его обработать — обособить каждое целое число (вещественные не трогаем) кавычками
# (добавить кавычку до и кавычку после элемента списка, являющегося числом) и дополнить нулём
# до двух целочисленных разрядов:
# ['в', '"', '05', '"', 'часов', '"', '17', '"', 'минут', 'температура', 'воздуха', 'была',
#  '"', '+05', '"', 'градусов']
# Сформировать из обработанного списка строку:
# в "05" часов "17" минут температура воздуха была "+05" градусов
# Подумать, какое условие записать, чтобы выявить числа среди элементов списка?
# Как модифицировать это условие для чисел со знаком?
# Примечание: если обособление чисел кавычками не будет получаться - можете вернуться к его
# реализации позже. Главное: дополнить числа до двух разрядов нулём!
# Домашняя работа к уроку №2 задание 3
# * (вместо задачи 2) Решить задачу 2 не создавая новый список (как говорят, in place).
# Эта задача намного серьёзнее, чем может сначала показаться.

my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была',
           '+5', 'градусов']
print(my_list, id(my_list))

# for i in range(len(my_list)):
#     try:
#         int(my_list[i])
#         if my_list[i].startswith('+'):
#             my_list[i] = f'"{my_list[i].zfill(3)}"'
#         elif my_list[i].isdecimal():
#             my_list[i] = f'"{my_list[i].zfill(2)}"'
#     except:
#         pass

for i in range(len(my_list)):
    if my_list[i].isdigit():
        my_list[i] = f'"{int(my_list[i]):02d}"'
    elif my_list[i][1:].isdecimal():
        my_list[i] = f'"{my_list[i][0]}{int(my_list[i][1:]):02d}"'

print(my_list, id(my_list))
print(' '.join(my_list), id(my_list))