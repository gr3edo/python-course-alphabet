import uuid
from objects_and_classes.homework.constants import CARS_TYPES, CARS_PRODUCER, TOWNS
"""
Вам небхідно написати 3 класи. Колекціонери Гаражі та Автомобілі.
Звязкок наступний один колекціонер може мати багато гаражів.
В одному гаражі може знаходитися багато автомобілів.

Автомобіль має наступні характеристики:
    price - значення типу float. Всі ціни за дефолтом в одній валюті.
    type - одне з перечисленних значеннь з CARS_TYPES в docs.
    producer - одне з перечисленних значеннь в CARS_PRODUCER.
    number - значення типу UUID. Присвоюється автоматично при створенні автомобілю.
    mileage - значення типу float. Пробіг автомобіля в кілометрах.


    Автомобілі можна перівнювати між собою за ціною.
    При виводі(logs, print) автомобілю повинні зазначатися всі його атрибути.

    Автомобіль має метод заміни номеру.
    номер повинен відповідати UUID

Гараж має наступні характеристики:

    town - одне з перечислениз значеннь в TOWNS
    cars - список з усіх автомобілів які знаходяться в гаражі
    places - значення типу int. Максимально допустима кількість автомобілів в гаражі
    owner - значення типу UUID. За дефолтом None.


    Повинен мати реалізованими наступні методи

    add(car) -> Добавляє машину в гараж, якщо є вільні місця
    remove(cat) -> Забирає машину з гаражу.
    hit_hat() -> Вертає сумарну вартість всіх машин в гаражі


Колекціонер має наступні характеристики
    name - значення типу str. Його ім'я
    garages - список з усіх гаражів які належать цьому Колекціонеру. Кількість гаражів за замовчуванням - 0
    register_id - UUID; Унікальна айдішка Колекціонера.

    Повинні бути реалізовані наступні методи:
    hit_hat() - повертає ціну всіх його автомобілів.
    garages_count() - вертає кількість гаріжів.
    сars_count() - вертає кількість машиню
    add_car() - додає машину у вибраний гараж. Якщо гараж не вказаний, то додає в гараж, де найбільше вільних місць.
    Якщо вільних місць немає повинне вивести повідомлення про це.

    Колекціонерів можна порівнювати за ціною всіх їх автомобілів.
"""


class Cesar:
    def __init__(self, name: str, garages=None):
        self.name = name
        self.garages = garages if garages else []
        self.register_id = uuid.uuid4()

    def hit_hat(self):
        return sum(garage.hit_hat() for garage in self.garages)

    def garages_count(self):
        return len(self.garages)

    def cars_count(self):
        return sum(len(garage.cars) for garage in self.garages)

    def add_car(self, garage=None):
        pass



class Car:
    def __init__(self, price: float, type: CARS_TYPES, producer: CARS_PRODUCER, mileage: float):
        self.price = price
        self.mileage = mileage
        self.number = uuid.uuid4()
        self.type = type if type in CARS_TYPES else []
        self.producer = producer if producer in CARS_PRODUCER else []

    def __repr__(self):
        return f"Car: price - {self.price}, type - {self.type}, producer - {self.producer}, mileage - {self.mileage}"

    def change_number(self):
        self.number = uuid.uuid4()

    def __eq__(self, other):
        return self.price == other.price

    def __ne__(self, other):
        return self.price != other.price

    def __gt__(self, other):
        return self.price > other.price

    def __ge__(self, other):
        return self.price >= other.price

    def __lt__(self, other):
        return self.price < other.price

    def __le__(self, other):
        return self.price <= other.price


class Garage:
    owner: uuid.UUID

    def __init__(self, town: TOWNS, places: int, owner=None, cars=[]):
        self.town = town if town in TOWNS else []
        self.cars = cars
        self.places = places
        self.owner = owner

    def add(self, car):
        if len(self.cars) < self.places:
            self.cars.append(car)
        else:
            print("Missing free space for the new car")

    def remove(self, car):
        self.cars.remove(car)

    def hit_hat(self):
        return sum(car.price for car in self.cars)
