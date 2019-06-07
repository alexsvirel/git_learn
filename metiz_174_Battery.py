""" Создаем класс атрибуты которого будут использованы в дурих классах"""

class Battery():
    """ Простая модел аккумулятора """
    def __init__(self, battery_size=70):
        """ Инициализирует атрибуты аккумулятора """
        self.battery_size = battery_size

    def describe_battery(self):
        """ Выводит информацию о мощности аккумулятора """
        print("Этот элетромобиль имеет батарею на " + str(self.battery_size) + " кВт")

    def get_range(self):
        """ Выводит примерный запас хода на аккумуляторе """
        range = 0
        if self.battery_size < 40:
            print("Надо зарядить аккумулятор")
        elif self.battery_size <= 70:
            range = 300
        elif self.battery_size <= 90:
            range = 400
        else:
            print("Так можно уехать далеко!")

        if range:
            print("Запас хода " + str(range) + " км")

    def upgrade_battery(self):
        """ Проверяет мощность аккумулятора в электромобиле и делает ее не меньше 85 кВт """
        if self.battery_size < 85:
            self.battery_size = 85
