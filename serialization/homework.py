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

from objects_and_classes.homework.homework import Cesar, Garage, Car


class SerCesar(Cesar):
    pass


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
    def from_json(cls, instance):
        if not isinstance(instance, dict):
            instance = json.loads(instance)

        number = instance['number']
        price = instance['price']
        car_type = instance['car_type']
        producer = instance['producer']
        mileage = instance['mileage']

        return cls(price=price, car_type=car_type, producer=producer, mileage=mileage, number=number)

    @classmethod
    def from_json_file(cls):
        with open("car_from_file.json", 'r') as file:
            instance = json.load(file)
        return cls.from_json(instance)

class SerGarage(Garage):
    pass


if __name__ == '__main__':
    car_1 = SerCar(200, "Diesel", "Ford", 4000)
    car_2 = SerCar(300, "Sedan", "Chery", 5000)
    car_3 = SerCar(400, "Coupe", "Dodge", 6000)
