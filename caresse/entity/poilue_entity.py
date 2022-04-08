import numpy as np

from .base_entity import BaseEntity


class PoilueEntity(BaseEntity):
    def __call__(self, x):
        assert isinstance(x, (int, float, complex, np.ndarray)), "`x` n'est pas un nombre."
        return x * 2
