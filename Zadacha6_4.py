class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
    def go(self):
        return f'{self.name} Поехали'
    def stop(self):
        return f'{self.name} Стоп машина'
    def turn_levo(self):
        return f'{self.name} Поворот налево'
    def turn_pravo(self):
        return f'{self.name} Поворот направо'
    def alarm(self):
        return f'{self.name} Включить мигалку'
    def show_speed(self):
        return f'Скорость {self.name} составила {self.speed} км/ч'

class TownCar(Car):
    def __init__(self, speed, color, name, is_police, passenger_capacity):
        super().__init__(speed, color, name, is_police)
        self.passenger_capacity = passenger_capacity

    def show_speed(self):
        print(f'Скорость {self.name} составила {self.speed} км/ч')
        if self.speed > 60:
            return (f'Скорость {self.name} превысила разрешенную для TownCar')
        else:
            return (f'Скорость {self.name} соответствует разрешенной для TownCar')
class SportCar(Car):
    def __init__(self, speed, color, name, is_police, motor_power):
        super().__init__(speed, color, name, is_police)
        self.motor_power = motor_power
class WorkCar(Car):
    def __init__(self, speed, color, name, is_police, body_volume):
        super().__init__(speed, color, name, is_police)
        self.body_volume = body_volume

    def show_speed(self):
        print(f'Скорость {self.name} составила {self.speed} км/ч')
        if self.speed > 40:
            return (f'Скорость {self.name} превысила разрешенную для WorkCar')
        else:
            return (f'Скорость {self.name} соответствует разрешенной для WorkCar')

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police,siren):
        super().__init__(speed, color, name, is_police)
        self.siren = siren

troleybas=TownCar(60,'blue','Troleybas',0,65)
print(troleybas.go())
print(troleybas.show_speed())

ferrary=SportCar(100,'red','Ferrary',0,1000)
print(ferrary.stop())

caterpillar=WorkCar(60,'yellow','Cat',0,453)
print(caterpillar.turn_levo()+' затем '+caterpillar.turn_pravo())
print(caterpillar.show_speed())

sheriff=PoliceCar(150,'blue and white','Sheriff',1,1)
print(sheriff.alarm())


