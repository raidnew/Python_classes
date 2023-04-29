#todo: Создать абстрактный класс Transport (транспорт) содержащий:
# Поля:
# скорость;
# себестоимость перевозки груза;
# стоимость перевозки груза.
# В классе должны быть абстрактные методы:
# метод Cost (без параметров) – вычисление стоимости перевозки груза.
# Метод Info - информация (без параметров), который возвращает строку, содержащую информацию об объекте.
#
# На его основе реализовать дочерние классы:
# Marine - морской транспорт,
# Ground - наземный транспорт.

from abc import ABC, abstractmethod

class Transport(ABC):

    name = None
    speed = None
    cost = None
    price = None

    @abstractmethod
    def Cost(self):
        pass

    @abstractmethod
    def Info(self):
        pass

    def print_info(self):
        print(f"{self.name} transport: Speed: {self.speed}  Cost: {self.cost}  Price: {self.price}")

class Marine(Transport):
    def __init__(self):
        self.name = "Marine"
        self.speed = 20

    def Cost(self):
        self.cost = 10
        self.price = 20

    def Info(self):
        self.print_info()

class Ground(Transport):
    def __init__(self):
        self.name = "Ground"
        self.speed = 50

    def Cost(self):
        self.cost = 20
        self.price = 30

    def Info(self):
        self.print_info()

marine_transport = Marine()
ground_transport = Ground()

marine_transport.Info()
ground_transport.Info()

marine_transport.Cost()
ground_transport.Cost()

marine_transport.Info()
ground_transport.Info()