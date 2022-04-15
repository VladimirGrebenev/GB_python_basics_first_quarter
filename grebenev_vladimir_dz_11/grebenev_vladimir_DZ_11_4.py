# Домашняя работа к уроку №11 задание 4-6
# Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определите параметры, общие для приведённых типов.
# В классах-наследниках реализуйте параметры, уникальные для каждого типа оргтехники.
# Продолжить работу над первым заданием. Разработайте методы, которые отвечают за приём оргтехники
# на склад и передачу в определённое подразделение компании. Для хранения данных о наименовании и
# количестве единиц оргтехники, а также других данных, можно использовать любую подходящую структуру
# (например, словарь).
# Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый
# тип данных.
# Подсказка: постарайтесь реализовать в проекте «Склад оргтехники» максимум возможностей, изученных
# на уроках по ООП.

class Storage:
    def __init__(self, storage_name):
        self.equipment = {}
        self.storage_name = storage_name

    def __str__(self):
        return f'{self.equipment}'

    @staticmethod
    def valid_quantity(qty):
        try:
            qty = int(qty)
        except Exception:
            print('Ошибка! Нужно ввести цифрами количество перемещаемых ценностей')
            qty = 0
        finally:
            return qty

    def accept_to_storage(self, eq_item, qty):
        '''приём/закупка оборудования в подразделение/на склад'''
        qty = self.valid_quantity(qty)
        if eq_item in self.equipment:
            self.equipment[eq_item] += qty
        else:
            self.equipment[eq_item] = qty
        print(f'->>>{self.storage_name} принял {eq_item.model} в количестве {qty}')

    def move_to_department(self, where_to, eq_item, qty):
        '''перемещение обрудования между подразделениями'''
        qty = self.valid_quantity(qty)
        if eq_item in self.equipment and (self.equipment[eq_item] - qty) >= 0:
            self.equipment[eq_item] -= qty
            where_to.accept_to_storage(eq_item, qty)
            print(f'перемещением с {self.storage_name}')
        else:
            print(f'->>> Техника {eq_item.model} отсутствует на {self.storage_name} в нужном '
                  f'количестве {qty}. Перемещение не удалось.')

    def report_storage(self):
        print(f'!>>> Отчёт материальных ценностей на {self.storage_name}')
        for eq_item in self.equipment:
            print(f'{eq_item.__dict__}, Количество на складе: {self.equipment[eq_item]}')

class Equipment:
    def __init__(self, model):
        self.model = model

class Printer(Equipment):
    def __init__(self, model, color='black'):
        super().__init__(model)
        self.color = color

class Scanner(Equipment):
    def __init__(self, model, wired='wifi'):
        super().__init__(model)
        self.wired = wired

class Xerox(Equipment):
    def __init__(self, model, mfu='МФУ'):
        super().__init__(model)
        self.mfu = mfu


p = Printer('Canon 2310')
s = Scanner('ScanJet 10')
x = Xerox('Xerox 4580', 'не МФУ')
big_storage = Storage('Big Storage')
workshop = Storage('Workshop №321')
big_storage.accept_to_storage(p, 20)
workshop.accept_to_storage(p, '20')
big_storage.move_to_department(workshop, p, 10)
big_storage.report_storage()
big_storage.move_to_department(workshop, p, 20)
workshop.report_storage()



