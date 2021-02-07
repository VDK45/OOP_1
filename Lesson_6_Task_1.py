import time


class TrafficLight:

    def __init__(self, c='Light'):
        self.__color = c
        print('Traffic Light added')

    def running(self, red, yellow, green):
        while True:
            if red.lower() != 'red':
                break
            print(f'{self.__color} {red}')
            time.sleep(7)
            if yellow.lower() != 'yellow':
                break
            print(f'{self.__color} {yellow}')
            time.sleep(2)
            if green.lower() != 'green':
                break
            print(f'{self.__color} {green}')
            time.sleep(7)


light_1 = TrafficLight('Lenin street')
light_1.running('Red', 'Yellow', 'Green')
