import caresse

print("BONCHOUUUUR")
print("Ici ce serait du code interpreter si: ")
print("  - j'importe `caresse.main` avec `from caresse import main`")
print("  - j'execute ce fichier avec `python -m caresse.main`")
print("ANR'VOIIIIR")

if __name__ == "__main__":

    print("\n # Un peu d'intropsection")
    print("version: ", caresse.__version__)  # 6.6.6
    print("file: ", caresse.__file__)  # /tmp/caresse/caresse/__init__.py
    print("path: ", caresse.__path__)  # ['/tmp/caresse/caresse']
    print("dir: ", dir(caresse))

    # exposer les sous-modules via le module principal `caresse`
    print("\n # `caresse/__init__.py` expose `entity` mais pas `vehicule`")

    print("`caresse.entity` possible?", "entity" in dir(caresse))  # True
    print("`caresse.vehicle` possible?", "vehicle" in dir(caresse))  # False

    print(
        "/!\\ Il se peut que `caresse.vehicle` ne plante pas dans certaines cas foireux, mais faut pas compter dessus."
    )

    # import des "sous-modules"
    print("\n # `caresse/entity/__init__.py` expose plusieurs objets/attributs")
    from caresse import entity

    print(dir(entity))  # pour avoir la liste de tous les trucs accessibles via `entity`
    print("\n # pareil pour `caresse/vehicle/__init__.py` expose plusieurs objets/attributs")

    from caresse import vehicle

    print(dir(vehicle))  # pour avoir la liste de tous les trucs accessibles via `entity`
    obj_OK = caresse.entity.BorgneEntity()
    print(obj_OK, dir(obj_OK))

    try:
        obj_not_OK = caresse.vehicle.FastKart()
    except AttributeError as e:
        print("error: ", e.args)
        print("Si tu veux que ça marche, il faut modifier le fichier `caresse/__init__.py`")
        obj_not_OK_but_OK = vehicle.FastKart()
        print(obj_not_OK_but_OK)

    # import d'un objet directement
    print(
        "\n # Pas besoin de tout exposer dans les `__init__.py` pour aller chercher les objets/attributs qui "
        + "t'intéressent. Les `__init__.py` restent nécessaires pour que les sous-dossiers sont reconnus commes des"
        + "sources du pacakge."
    )
    from caresse.entity.poilue_entity import PoilueEntity

    pe = PoilueEntity()
    print(pe, pe(5))

    from caresse.vehicle import FastKart

    fc = FastKart()
    print(fc, fc.speed)

    from caresse.utils import norm_2D

    phi = norm_2D([1, 1])
    print(phi)
