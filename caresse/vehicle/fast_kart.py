from .base_vehicle import BaseVehicule


class FastKart(BaseVehicule):
    def move(self, direction, dt):
        self.position += (self.speed * direction) / dt

    @property
    def speed(self):
        return 10.0
