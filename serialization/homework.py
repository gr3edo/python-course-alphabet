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
import random
import uuid

from ruamel.yaml import YAML

from objects_and_classes.homework.constants import CARS_PRODUCER, CARS_TYPES, TOWNS
from objects_and_classes.homework.homework import Cesar, Garage, Car


# yaml
class SerCesar(Cesar):
    yaml = YAML()

    def dict(self):
        data = {'name': self.name, 'register_id': str(self.register_id),
                'garages': [garage.to_dict() for garage in self.garages] if self.garages else [], }

        return data

    def to_yaml(self):
        return self.yaml.dump(self.dict())

    def to_yaml_file(self):
        with open("cesar_to_yaml.yaml", 'w') as file:
            self.yaml.dump(self.dict(), file)


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
        with open("car_from_file.json", 'r') as file:
            instance = json.load(file)
        return cls.from_json(instance)


# pickle
class SerGarage(Garage):
    def dict(self):
        data = {'town': self.town, 'places': self.places, 'owner': self.owner, 'cars': []}

        if isinstance(self.owner, uuid.UUID):
            data['owner'] = str(self.owner)

        for car in self.cars.values():
            data['cars'].append(car.to_dict())

        return data


if __name__ == '__main__':
    car1 = SerCar(price=random.randint(5000, 50000), car_type=random.choice(CARS_TYPES),
                  producer=random.choice(CARS_PRODUCER), mileage=random.randint(1000, 5000))
    car2 = SerCar(price=random.randint(5000, 50000), car_type=random.choice(CARS_TYPES),
                  producer=random.choice(CARS_PRODUCER), mileage=random.randint(1000, 5000))
    car3 = SerCar(price=random.randint(5000, 50000), car_type=random.choice(CARS_TYPES),
                  producer=random.choice(CARS_PRODUCER), mileage=random.randint(1000, 5000))
    car4 = SerCar(price=random.randint(5000, 50000), car_type=random.choice(CARS_TYPES),
                  producer=random.choice(CARS_PRODUCER), mileage=random.randint(1000, 5000))

    garage1 = SerGarage(town=random.choice(TOWNS), places=2)
    garage2 = SerGarage(town=random.choice(TOWNS), places=3)
    garage3 = SerGarage(town=random.choice(TOWNS), places=4)

    cesar1 = SerCesar(name="Ivan")

    cesar1.add_car(car1, garage1)
    cesar1.add_car(car2, garage1)
    cesar1.add_car(car3, garage2)
    cesar1.add_car(car4, garage3)

    cesar1.to_yaml_file()
