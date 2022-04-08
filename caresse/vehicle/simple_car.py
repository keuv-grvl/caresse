from .base_vehicle import BaseVehicule


class SimpleCar(BaseVehicule):
    def __init__(self):
        super().__init__()
        self.frottements = 0.96

    def move(self, direction, dt):
        self.position += (self.frottements * self.speed * direction) / dt

    @property
    def speed(self):
        return 7.0
