# Домашняя работа к уроку №9 задание 1
# Создать класс TrafficLight (светофор).
# определить у него один атрибут color (цвет) и метод running (запуск);
# атрибут реализовать как приватный;
# в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
# продолжительность первого состояния (красный) составляет 7 секунд, второго (жёлтый) — 2 секунды,
# третьего (зелёный) — на ваше усмотрение;
# переключение между режимами должно осуществляться только в указанном порядке (красный, жёлтый, зелёный);
# проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов. При его нарушении выводить соответствующее
# сообщение и завершать скрипт.

from time import sleep

class TrafficLight:
    __color = "цвет"
    def running(self):
        while True:
            __color = "красный"
            print(__color)
            sleep(7)
            __color = "жёлтый"
            print(__color)
            sleep(2)
            __color = "зелёный"
            print(__color)
            sleep(3)

sverofor = TrafficLight()
sverofor.running()


