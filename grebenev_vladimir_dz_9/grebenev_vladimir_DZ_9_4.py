# Домашняя работа к уроку №6 задание 4
# Реализуйте базовый класс Car.
# у класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась,\
#                                                                                повернула (куда);
# опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
# для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar)
# и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите
# результат. Вызовите методы и покажите результат.

class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = bool(is_police)

    def go(self):
        return print(f'машина {self.name} поехала')

    def stop(self):
        return print(f'машина {self.name} остановилась')

    def turn(self, direction):
        return print(f'машина {self.name} повернула {direction}')

    def show_speed(self):
        return print(f'скороть машины {self.name} равна {self.speed}')

class TownCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 60:
            self.is_police = True
            return print(f'машина {self.name} превысила скорость 60 км/ч')
        else:
            return print(f'скороть машины {self.name} равна {self.speed}')

class SportCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)

class WorkCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 40:
            self.is_police = True
            return print(f'машина {self.name} превысила скорость 40 км/ч')
        else:
            return print(f'скороть машины {self.name} равна {self.speed}')

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)

toyota = TownCar(60, 'white', 'Toyota Rav 4')
print(toyota.speed)
print(toyota.is_police)
toyota.speed = 65
toyota.show_speed()
print(toyota.is_police)

ferrari = SportCar(300, 'red', 'Ferrari F40')
print(ferrari.__dict__)
ferrari.show_speed()

gazel = WorkCar(35, 'black', 'Gazel')
gazel.show_speed()
gazel.stop()
gazel.go()
gazel.turn('направо')
gazel.speed = 45
gazel.show_speed()
