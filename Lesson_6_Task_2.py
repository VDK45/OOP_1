class Road:
    def __init__(self, l, w):
        self._length = l
        self._width = w
        print(f"Дорога длина в {l}м и шинина в {w}м ")

    def resul(self, weigth=25, tickness=5):
        res = (self._length * self._width * weigth * (tickness / 100)) / 1000
        print(f"Потребует {int(res)}тон асфальта если {weigth}кг на 1кв метра дороги толщиной в {tickness}см  ")


road_1 = Road(40, 500)
road_1.resul()
