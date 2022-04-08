from .base_vehicle import BaseVehicule


class GiganticRocket(BaseVehicule):
    def __init__(self):
        super().__init__()
        self.carburant = 10000.0

    def move(self, direction, dt):
        self.position += (self.frottements, self.speed * direction) / dt
        self.carburant -= 100.0

    @property
    def speed(self):
        return 700.0
