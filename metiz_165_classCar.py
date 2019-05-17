# класс представляющий автомобиль

class Car():
    """ Простая модель автомбиля """
    def __init__(self, make, model, year):
        """ Инициализирует атрибуты автомобиля """
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """ Возвращает отформатированное описание автомобиля """
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        """ выводит пробег автомобиля"""
        print("Этот автомобиль имеет пробег " + str(self.odometer_reading) + " км.")

    def updete_odometer(self, mileage):
        """ Устанавливает новое значение пробега """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("Нельзя уменьшать значение пробега")

    def increment_odometer(self, miles):
        if miles > 0:
            self.odometer_reading += miles
        else:
            print("Нельзя уменьшать значение пробега")

my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

print("Установим пробег в 23 км:")
# Изменение атрибута прямое (лучше не применять)
my_new_car.odometer_reading = 23
my_new_car.read_odometer()
# Изменение атрибута через функцию замены
print("Попытка установить пробег 20 км (меньше чем был):")
my_new_car.updete_odometer(20)
my_new_car.read_odometer()
print("Установим пробег в 200 км:")
my_new_car.updete_odometer(200)
my_new_car.read_odometer()
print("Увеличим пробег на -100 км:")
my_new_car.increment_odometer(-100)
my_new_car.read_odometer()
print("Увеличим пробег на 100 км:")
my_new_car.increment_odometer(100)
my_new_car.read_odometer()