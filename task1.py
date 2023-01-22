import doctest


class Table:
    def __init__(self, lenght: int, hight: int):
        """
        Описание объекта "стол"
        :param lenght: Длина стола
        :param hight: Высота стола
        Примеры:
        >>> table = Table(100, 900)  # инициализация экземпляра класса
        """
        if not isinstance(lenght, (int)):
            raise TypeError("Параметр длина должен быть типа int")
        if lenght <= 0:
            raise ValueError("Параметр длина должен быть положительным числом")
        self.volume_of_transported_concrete_mix = lenght

        if not isinstance(hight, int):
            raise TypeError("Параметр высота должен быть int")
        if hight < 0:
            raise ValueError("Параметр высота не может быть отрицательным числом")
        self.transportation_distance = hight

    def reached_maximum_hight(self) -> bool:
        """
        Функция которая проверяет, не превышает ли высота стола максимально возможной отметки
        :return: Достаточно ли стол низок
        Примеры:
        >>> table = Table(100, 900)
        >>> table.reached_maximum_hight()
        """
        ...

    def increase_hight_of_table(self, inc_hight: int) -> None:
        """
        Увеличение высоты стола.
        :param inc_hight: Увеличение высоты стола на данное значение
        :raise ValueError: Если стол не имеет возможности увеличиться еще больше
        Примеры:
        >>> table = Table(100, 800)
        >>> table.increase_hight_of_table(10)
        """
        if not isinstance(inc_hight, int):
            raise TypeError("Параметр значения увеличения высоты стола должен быть типа int")
        if inc_hight < 0:
            raise ValueError("Параметр значения увеличения высоты стола должен быть положительным числом")
        ...

    def decrease_hight_of_table(self, dec_hight: int) -> None:
        """
        Уменьшение высоты стола.
        :param inc_hight: Уменьшение высоты стола на данное значение
        :raise ValueError: Если стол не имеет возможности уменьшиться еще больше
        :return: Высота понижение стола. 
        Примеры:
        >>> table = Table(100, 900)
        >>> table.decrease_hight_of_table(1)
        """
        if not isinstance(dec_hight, int):
            raise TypeError("Параметр значения уменьшения высоты стола должен быть типа int")
        if dec_hight < 0:
            raise ValueError("Параметр значения уменьшения высоты стола должен быть положительным числом")
        ...


class Basketball:
    def __init__(self, pressure: float, diameter: float):
        """
        Описание объекта "Баскетбольный мяч"
        :param pressure: Давление в мяче
        :param diameter: Диаметр мяча
        Примеры:
        >>> ball = Basketball(0.62, 780)  # инициализация экземпляра класса
        """
        if not isinstance(pressure, (int, float)):
            raise TypeError("Давление в мяче должно быть типа int или float")
        if pressure <= 0:
            raise ValueError("Давление в мяче должно быть положительным числом")
        self.weight = pressure

        if not isinstance(diameter, (int, float)):
            raise TypeError("Диаметр мяча должен быть int или float")
        if diameter <= 0:
            raise ValueError("Диаметр мяча должен быть положительным числом")
        self.diameter = diameter

    def decreases_pressure (self, lvl_of_pressure_release: float) -> None:
        """
        Поиск меньшего мяча.
        :param lvl_of_pressure_release: Значение уменьшения давления в мяче
        :return: Если уменьшение давления будет создавать отрицательное давление в мяче, возвращается ошибка.
        Примеры:
        >>> ball = Basketball(0.1, 780)
        >>> ball.decreases_pressure(0.2)
        """
        if not isinstance(lvl_of_pressure_release, (int, float)):
            raise TypeError("Спуск давления должен быть типа int или float")
        if lvl_of_pressure_release < 0:
            raise ValueError("Спуск давления не может быть отрицательным числом")
        ...

    def is_deflated(self) -> bool:
        """
        Функция которая проверяет, сдут ли мяч
        :return: Сдулся ли мяч
        Примеры:
        >>> ball = Basketball(0.2, 780)
        >>> ball.is_deflated()
        """
        ...


class Car:
    def __init__(self, length_of_car: float, width_of_car: float, number_of_seats: int):
        """
        Описание объекта "легковой автомобиль"
        :param length_of_car: Длина автомобиля
        :param width_of_car: Ширина автомобиля
        :param number_of_seats: Кол-во мест в автомобиле
        Примеры:
        >>> car = Car(4.2, 2.2, 8)  # инициализация экземпляра класса
        """
        if not isinstance(length_of_car, (int, float)):
            raise TypeError("Длина автомобиля должна быть типа int или float")
        if length_of_car <= 0:
            raise ValueError("Длина автомобиля не может быть отрицательным числом")
        self.length_of_car = length_of_car

        if not isinstance(width_of_car, (int, float)):
            raise TypeError("Ширина автомобиля должна быть типа int или float")
        if width_of_car <= 0:
            raise ValueError("Ширина автомобиля не может быть отрицательным числом")
        self.width_of_car = width_of_car

        if not isinstance(number_of_seats, int):
            raise TypeError("Кол-во мест в автомобиле должно быть типа int")
        if number_of_seats <= 0:
            raise ValueError("Кол-во мест в автомобиле не может быть отрицательным числом")
        self.number_of_seats = number_of_seats

    def is_sportcar(self) -> bool:
        """
        Функция, которая проверяет является ли автомобиль спортивным.
        :return: Является ли опалубка несъемной
        Примеры:
        >>> car = Car(4.2, 2.2, 2)
        >>> car.is_sportcar()
        """
        ...

    def installation_of_extraseats(self, number_of_adding_seats: int) -> None:
        """
        Установка дополнительных мест.
        :param number_of_adding_seats: Кол-во дополнительных мест
        :return: Если кол-во добавляемых мест превышает их общее кол-во максимального, то возвращает ошибку.
        Примеры:
        >>> car = Car(4.2, 2.2, 4)
        >>> car.installation_of_extraseats(2)
        """
        if not isinstance(number_of_adding_seats, int):
            raise TypeError("Кол-во дополнительных мест должно быть типа int")
        if number_of_adding_seats <= 0:
            raise ValueError("Кол-во дополнительных мест не может быть отрицательным числом")
        ...


if __name__ == "__main__":
    doctest.testmod()
    pass