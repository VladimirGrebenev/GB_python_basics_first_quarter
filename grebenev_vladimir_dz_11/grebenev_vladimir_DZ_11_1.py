# Домашняя работа к уроку №11 задание 1
# Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата
# «день-месяц-год». В рамках класса реализовать два метода. Первый, с декоратором @classmethod.
# Он должен извлекать число, месяц, год и преобразовывать их тип к типу «Число». Второй,
# с декоратором @staticmethod, должен проводить валидацию числа, месяца и года
# (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.

class Data:
    def __init__(self, data_str):
        """data_str принимает строку в формате 'день-месяц-год'"""
        self.data_str = data_str

    @classmethod
    def data_to_int(cls, data_str):
        my_int_list = [int(item) for item in data_str.split('-')]
        return my_int_list

    @staticmethod
    def real_date_check(data_str):
        check_int_list = Data.data_to_int(data_str)
        if check_int_list[0] <= 0 or check_int_list[0] > 31:
            print('не верная дата, число должно быть от 1 до 31')
        elif check_int_list[1] <=0 or check_int_list[1] > 12:
            print('не верный месяц, число должно быть от 1 до 12')
        elif check_int_list[2] <=0:
            print('не верный год, число должно быть больше нуля')
        else:
            print('день-месяц-год введены корректно')


new_data = Data('18-03-1981')
print(new_data.data_str)
print(new_data.data_to_int(new_data.data_str))
print(Data.data_to_int('13-07-2018'))
Data.real_date_check('13-07-2018')
new_data.real_date_check('13-01-0')



