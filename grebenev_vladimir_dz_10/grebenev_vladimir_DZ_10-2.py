# Домашняя работа к уроку №10 задание 2
# Реализовать проект расчёта суммарного расхода ткани на производство одежды. Основная сущность (класс) этого
# проекта — одежда, которая может иметь определённое название. К типам одежды в этом проекте относятся пальто и
# костюм. У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть
# обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма
# (2*H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать
# абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.

from abc import ABC, abstractmethod

class Clohes(ABC):

    @abstractmethod
    def fabric_consume(self):
        pass

class Coat(Clohes):
    def __init__(self, size):
        super().__init__()
        self.size = size

    @property
    def fabric_consume(self):
        return round(self.size/6.5 + 0.5, 2)

class Suit(Clohes):
    def __init__(self, height):
        super().__init__()
        self.height = height

    @property
    def fabric_consume(self):
        return round(self.height * 2 + 0.3, 2)

my_coat = Coat(10)
print(my_coat.fabric_consume)
my_suit = Suit(20)
print(my_suit.fabric_consume)
print(round(my_suit.fabric_consume + my_coat.fabric_consume, 2))