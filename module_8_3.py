# Задача "Некорректность":

class Car:

    def __init__(self, model, vin, numbers):
        self.model = model
        self.__vin = vin
        self.__numbers = numbers

    @property
    def vin(self):
        return self.__vin

    def __is_valid_vin(self, vin_number):
        if not isinstance(vin_number, int):
            raise IncorrectVinNumber("Некорректный тип VIN-номера")
        elif vin_number < 1000000 or vin_number > 9999999:
            raise IncorrectVinNumber("VIN-номер должен быть в диапазоне от 1 000 000 до 9 999 999 включительно")
        else:
            return True

    @vin.setter
    def vin(self, new_vin):
        valid = self.__is_valid_vin(new_vin)
        if valid:
            self.__vin = new_vin
        else:
            raise IncorrectVinNumber(f"Некорректный VIN-номер {new_vin}")

    def __is_valid_numbers(self, numbers):
        if not isinstance(numbers, str):
            raise IncorrectCarNumbers("Номера автомобиля должны быть строкового типа")
        elif len(numbers) != 6:
            raise IncorrectCarNumbers("Номер автомобиля должен состоять из 6 символов")
        else:
            return True

    def numbers(self, new_numbers):
        valid = self.__is_valid_numbers(new_numbers)
        if valid:
            self.__numbers = new_numbers
        else:
            raise IncorrectCarNumbers(f"Номера автомобиля {new_numbers} некорректны")


class IncorrectVinNumber(Exception):
    def __init__(self, message):
        super().__init__()
        self.message = message


class IncorrectCarNumbers(Exception):
    def __init__(self, message):
        super().__init__()
        self.message = message


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
