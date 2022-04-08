from abc import ABC, abstractmethod


class BaseEntity(ABC):
    @abstractmethod
    def __call__(self, x):
        """TO BE DEFINED"""
