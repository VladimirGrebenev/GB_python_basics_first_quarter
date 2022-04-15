# Домашняя работа к уроку №11 задание 4
# Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определите параметры, общие для приведённых типов.
# В классах-наследниках реализуйте параметры, уникальные для каждого типа оргтехники.


class Storage:
    def __init__(self, storage_name):
        self.equipment = {}
        self.storage_name = storage_name

    def __str__(self):
        return f'{self.equipment}'

    def accept_to_storage(self, eq_item):
        '''приём/закупка оборудования в подразделение/на склад'''
        if eq_item in self.equipment:
            self.equipment[eq_item] += 1
        else:
            self.equipment[eq_item] = 1
        print(f'->>>{self.storage_name} принял {eq_item.model}')

    def move_to_department(self, where_to, eq_item):
        '''перемещение обрудования между подразделениями'''
        if eq_item in self.equipment and self.equipment[eq_item] != 0:
            self.equipment[eq_item] -= 1
            where_to.accept_to_storage(eq_item)
            print(f'перемещением с {self.storage_name}')
        else:
            print(f'->>>техника {eq_item.model} отсутствует на {self.storage_name}')

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
big_storage.accept_to_storage(p)
workshop.accept_to_storage(p)
big_storage.move_to_department(workshop, p)
big_storage.report_storage()
big_storage.move_to_department(workshop, p)
workshop.report_storage()



