import caresse


def test_init():
    assert caresse.__version__ == "6.6.6"
    assert caresse.__file__.endswith("caresse/caresse/__init__.py")
    assert caresse.__path__[0].endswith("caresse/caresse")


def test_instanciate_01():
    obj = caresse.vehicle.FastKart()
    # ça foire et c'est normal pour la démo
    assert obj.speed == 10.0


def test_instanciate_02():
    obj = caresse.entity.ChauveEntity()
    assert obj(-5) == 5


def test_instanciate_03():
    from caresse.vehicle import FastKart

    obj = FastKart()
    assert obj.speed == 10.0


def test_instanciate_04():
    from caresse.entity import ChauveEntity

    obj = ChauveEntity()
    assert obj(-5) == 5
