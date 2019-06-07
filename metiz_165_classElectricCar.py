""" Наследование классов """

from metiz_165_classCar import Car
from metiz_174_Battery import Battery

class ElectricCar(Car):
    """ Представляет аспекты специфические для электромобилей """
    def __init__(self, make, model, year):
        """ Инициализирует атрибуты класса-родителя """
        super().__init__(make, model, year)
        self.battery = Battery(15)

    def fill_gas_tank(self, *liters):
        """ Переопределяет меторд родительского класса
            в электромобилях нет бензобака """
        print("В электромобилях " + self.make.title() + " нет бензобака")


my_audi = Car('audi', 'a4', 2010)
my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.fill_gas_tank()
my_audi.fill_gas_tank(50)
my_tesla.battery.get_range()
my_tesla.battery.upgrade_battery()
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()