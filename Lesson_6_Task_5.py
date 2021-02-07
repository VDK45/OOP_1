class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return print(f'Запуск отрисовки {self.title} ')


class Pen(Stationery):
    def draw(self):
        return print(f'{self.title} пишет')


class Pencil(Stationery):
    def draw(self):
        return print(f'{self.title} рисует')


class Handle(Stationery):
    def draw(self, title):  # ???
        self.title = 'Маркер'
        return print(f'{self.title} красит')


a = Stationery('с инструментами')
a.draw()
b = Pen('Ручка')
b.draw()
c = Pencil('Карандаш')
c.draw()
d = Handle('')
d.draw('')
