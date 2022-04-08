__version__ = "6.6.6"
__doc__ = """
The help message when you type
    >>> import caresse
    >>> help(caresse)
"""

from . import entity  # import le dossier `entity`, qui va par défaut aller lire `entity.__init__.py`
from . import utils
from .utils import distance, norm_2D

# from . import vehicle

__all__ = ["distance", "norm_2D", "utils", "entity"]  # , "vehicle"]
