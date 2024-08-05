class IncorrectCarNumbers(Exception):
    def __init__(self):
        self.message = 'Неверная длина номера'

    def __str__(self):
        return self.message

class IncorrectVinNumber(Exception):
    def __init__(self):
        self.message = 'Неверный диапазон для vin номера'

    def __str__(self):
        raise self.message

class Car:
    def __init__(self, model, vin, numbers):
        self.model = model
        self.__vin = vin
        self.__numbers = numbers
        self.__is_valid_vin()
        self.__is_valid_numbers()

    def __is_valid_vin(self):
        if self.__vin >= 1000000 and self.__vin <= 9999999 and type(self.__vin) is int :
            return True
        else:
            raise IncorrectVinNumber


    def __is_valid_numbers(self):
        if type(self.__numbers) is str and len(self.__numbers) == 6:
            return True
        else:
            raise IncorrectCarNumbers



try:
  first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{first.model} успешно создан')

try:
  second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{second.model} успешно создан')

try:
  third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{third.model} успешно создан')
