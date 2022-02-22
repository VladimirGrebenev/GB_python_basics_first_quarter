# # Geek University Python-разработки - первая четверть - Основы языка Python.
# # Домашняя работа к уроку №1 задание 2
# Создать список, состоящий из кубов нечётных чисел от 1 до 1000 (куб X - третья степень числа X):
# Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7. Например, число
# «19 ^ 3 = 6859» будем включать в сумму, так как 6 + 8 + 5 + 9 = 28 – делится нацело на 7. Внимание:
# использовать только арифметические операции!
# К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из этого списка, сумма цифр
# которых делится нацело на 7.
# * Решить задачу под пунктом b, н

in_a_cube = []
[in_a_cube.append(el**3) for el in range(1, 1001, 2)]

def devided_list(your_list, divider):
    """функция принимает на вход список чисел your_list и возвращает список чисел которые делятся без остатка
    на divider"""
    new_list = []
    [new_list.append(el) for el in your_list if sum(map(int, list(str(el)))) % divider == 0]
    return new_list

divided_seven = devided_list(in_a_cube, 7)

for i in range(len(divided_seven)):
    divided_seven[i] += 17

print(sum(divided_seven))
print(sum(devided_list(divided_seven, 7)))