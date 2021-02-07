class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return print(f"{self.name} {self.color} едет вперед ")

    def stop(self):
        return print(f"{self.name} {self.color}  остановилась")

    def turn_left(self):
        return print(f"{self.name} {self.color} поворачивает налево")

    def turn_right(self):
        return print(f"{self.name} {self.color} поворачивает направо")


class TownCar(Car):
    def __init__(self, speed, color, name, is_police, show_sp=True):
        super().__init__(speed, color, name, is_police)
        self.show_sp = show_sp
        print('TownCar car')

    def show_speed(self):
        if self.speed > 60:
            return print(f"{self.name}  {self.color}  {self.speed}km/h  превышает 60 км/ч!!!!!!!!")
        else:
            return print(f"{self.name}  {self.color}  едет со скоростью {self.speed}km/h, нет превышения скорости")


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police, show_sp=True):
        super().__init__(speed, color, name, is_police)
        self.show_sp = show_sp
        print('Work Car')

    def show_speed(self):
        if self.speed > 40:
            return print(f"{self.name}  {self.color}  {self.speed}km/h  превышает 40 км/ч!!!!!!!!")
        else:
            return print(f"{self.name}  {self.color}  едет со скоростью {self.speed}km/h, нет превышения скорости")


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
        print('Sport car')

    def show_speed(self):
        return print(f"{self.name}  {self.color}  едет со скоростью {self.speed}km/h")


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police=True)
        print('Police car')

    def show_speed(self):
        return print(f"{self.name}  {self.color}  едет со скоростью {self.speed}km/h")


auto_1 = TownCar(66, "белая", "Toyota", False, True)
auto_1.go()
auto_1.show_speed()
auto_2 = SportCar(140, "черный", "Mustang", False)
auto_2.turn_left()
auto_2.turn_right()
auto_2.show_speed()
auto_3 = PoliceCar(70, "Белая", "Лада", True)
auto_3.show_speed()
auto_3.go()
auto_4 = WorkCar(35, 'серый', 'Камаз', False)
auto_4.go()
auto_4.show_speed()
