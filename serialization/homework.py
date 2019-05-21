"""
Для попереднього домашнього завдання.
Для класу Колекціонер Машина і Гараж написати методи, які створюють інстанс обєкту
з (yaml, json, pickle) файлу відповідно

Для класів Колекціонер Машина і Гараж написати методи, які зберігають стан обєкту в файли формату
yaml, json, pickle відповідно.

Для класів Колекціонер Машина і Гараж написати методи, які конвертують обєкт в строку формату
yaml, json, pickle відповідно.

Для класу Колекціонер Машина і Гараж написати методи, які створюють інстанс обєкту
з (yaml, json, pickle) строки відповідно


Advanced
Добавити опрацьовку формату ini

"""
import json
import pickle
import uuid

from ruamel import yaml
from ruamel.yaml import YAML

from objects_and_classes.homework.homework import Cesar, Garage, Car


# yaml
class SerCesar(Cesar):
    yaml = YAML()

    def dict(self):
        data = {'name': self.name, 'register_id': str(self.register_id),
                'garages': [garage.dict() for garage in self.garages] if self.garages else [], }

        return data

    @staticmethod
    def from_yaml_string(data):
        return SerCesar.from_yaml(yaml.load(data))

    def to_yaml(self):
        return yaml.dump(self.dict())

    def to_yaml_file(self):
        with open("cesar_to_yaml.yaml", 'w') as file:
            self.yaml.dump(self.dict(), file)

    @classmethod
    def from_yaml(cls, data):
        name = data['name']
        garages = [SerGarage.from_yaml_string(data) in data['garages']]
        return SerCesar(name=name, garages=garages)

    def instance_from_yaml_string(obj, yaml_string: str):
        return obj.from_yaml(yaml.load(yaml_string))

    @staticmethod
    def from_yaml_file():
        with open("cesar_to_yaml.yaml", 'r') as file:
            return SerCesar.from_yaml(yaml.load(file))


# json
class SerCar(Car):

    def dict(self):
        return {'price': self.price, 'car_type': self.car_type, 'producer': self.producer, 'mileage': self.mileage,
                'number': str(self.number)}

    def to_json(self):
        return json.dumps(self.dict())

    def to_json_file(self):
        with open("car_to_file.json", 'w') as file:
            json.dump(self.dict(), file)

    @classmethod
    def from_json(cls, data):
        if not isinstance(data, dict):
            data = json.loads(data)

        number = data['number']
        price = data['price']
        car_type = data['car_type']
        producer = data['producer']
        mileage = data['mileage']

        return cls(price=price, car_type=car_type, producer=producer, mileage=mileage, number=number)

    @classmethod
    def from_json_file(cls):
        with open("car_to_file.json", 'r') as file:
            instance = json.load(file)
        return cls.from_json(instance)


# pickle
class SerGarage(Garage):
    def dict(self):
        data = {'town': self.town, 'places': self.places, 'owner': self.owner,
                'cars': [car.dict() for car in self.cars] if self.cars else [], }

        if isinstance(self.owner, uuid.UUID):
            data['owner'] = str(self.owner)
        return data

    def to_pickle(self):
        return pickle.dumps(self)

    def to_pickle_file(self):
        with open("garage_to_pickle", 'wb') as file:
            pickle.dump(self, file)

    @staticmethod
    def from_pickle(data):
        return pickle.loads(data)

    @staticmethod
    def from_pickle_file():
        with open("garage_to_pickle", 'rb') as file:
            data = pickle.load(file)
        return data

    def to_yaml_string(self):
        garage_yaml_string = self.to_yaml()
        return str(garage_yaml_string)

    def to_yaml(obj):
        cars = [car.to_json_string() for car in obj.cars]
        data = {"cars": cars, "places": obj.places, "town": obj.town, "owner": str(obj.owner)}
        return data

    @staticmethod
    def from_yaml_string(data):
        return SerGarage.from_yaml(data)

    @staticmethod
    def from_yaml(data):
        cars = data['cars']
        places = data['places']
        town = data['town']
        owner = data['owner']
        return SerGarage(cars=cars, places=places, town=town, owner=owner)
