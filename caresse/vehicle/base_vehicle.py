from abc import ABC, abstractmethod


class BaseVehicule(ABC):
    @abstractmethod
    def move(self):
        """move your vehicle"""

    @property
    @abstractmethod
    def speed(self):
        """return the current speed in m/s"""
