# # Geek University Python-разработки - первая четверть - Основы языка Python.
# # Домашняя работа к уроку №5 задание 2
# * (вместо 1) Решить задачу генерации нечётных чисел от 1 до n (включительно), не используя ключевое слово yield.

max_num = 15
num_gen = (num for num in range(1, max_num+1, 2))

print(next(num_gen))
print(next(num_gen))
print(next(num_gen))

