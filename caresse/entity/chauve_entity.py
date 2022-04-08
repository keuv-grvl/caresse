from .base_entity import BaseEntity


class ChauveEntity(BaseEntity):
    def __call__(self, x):
        return -x
