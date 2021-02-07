class Worker:
    def __init__(self, name: str, surname: str, position: str, wage: int, bonus: int):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}
        print('Добавлен  сотрудник: ')


class Position(Worker):
    def get_full_name(self):
        return print(f"{self.position}:  {self.name} {self.surname}")

    def get_total_income(self):
        total = sum(self._income.values())
        return print(f"{self.name} {self.surname} получает {total} рублей")


person_1 = Position('Евгений', 'Колмаков', 'Директор', 600000, 567899)
person_1.get_full_name()
person_1.get_total_income()

person_2 = Position('Иван', 'Иванов', 'Менежер', 300000, 45899)
person_2.get_full_name()
person_2.get_total_income()
