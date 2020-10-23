class Road:
    def __init__(self, _length, _width):
        self._length = _length
        self._width = _width

    def mass(self):
        return ves*toljina*self._length * self._width/100000

ves=25
toljina=5

road = Road(20, 5000)
print('Необходимая масса асфальта для покрытия',road.mass(),'т')
