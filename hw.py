class Vehicle:

    def __init__(self, owner, model, color, engine_power):
        self.owner = owner
        self.__model = model
        self.__engine_power = engine_power
        self.color = color
        self.cv = _COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']

    def get_model(self):
        return self.__model

    def get_horsepower(self):
        return self.__engine_power

    def get_color(self):
        return self.color

    def get_owner(self):
        return self.owner
    def print_info(self):
        print(f'Модель: {self.get_model()}\n Мощность двигателя: {self.get_horsepower()}\n Цвет: {self.get_color()}\n Владелец: {self.get_owner()}')

    def set_color(self, color):
        if color.lower() in self.cv:
            self.color = color
        else:
            print(f'Нельзя сменить цвет на {color}')

class Sedan(Vehicle):
    _PASSAGERS_LIMIT = 5

# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()

