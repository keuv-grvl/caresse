# caresse

> Démo de package Python.

Ici, tout le code est regroupé dans le dossier `caresse` et les sous-dossiers `entity` et `vehicle` pourraient être tes
`app` et `app2`.


## Installation

```bash
pip install -e .
pip install -e '.[dev]'  # install additionnal deps
```

`.` signifie que `pip` va chercher un fichier `setup.py` dans le dossier courant et l'installer.

`-e` permet d'installer le package comme les autres packages, mais avec ses sources dans le dossier courant.
C'est-à-dire que les modifs dans le code local seront répercutées à l'utilisation du package.

`[dev]` c'est le ptit bonus qui fait plaisir, ça installer des dépendances supplémentaires (ici, de quoi formatter ton
code).


## Inspect

Une fois installé, le package peut être utilisé comme n'importe quel package:

```python
import caresse
print(caresse.__version__)  # 6.6.6
chauve = caresse.entity.ChauveEntity()
chauve.__call__(-5)  # 5
chauve(-5)  # identique à la ligne d'avant
```

Plus d'exemples dans `caresse/__main__.py`.


## Exécution

Tu dois être dans le bon dossier pour que ça marche, ou mettre un chemin complet :

```bash
$ python caresse/__main__.py
```

Ça marche quelque soit ton répértoire courant (puisque tu as pip-installé le package) :

```bash
$ python -m caresse  # qui va aller lire le fichier `caresse/__main__.py` directement
```

Si jamais tu veux 2 app indépendantes, tu peux créer un fichier `caresse/vehicle/__main__.py` et
`caresse/entity/__main__.py`, qui font chacun leur café, et que tu pourras éxecuter avec :

```bash
$ python -m caresse.entity
$ python -m caresse.vehicle
```

Si tu veux 2 executable différents rangés dans `caresse/entity`, tu peux créer des fichiers
`caresse/entity/exec1.py` et `caresse/entity/mon_programme.py`, que tu executeras via:

```bash
python -m caresse.entity.exec1
python -m caresse.entity.mon_programme
```



## Cadeaux Bonux

Le `Makefile` permet d'automatiser ~~un chiée~~ pléthore de trucs pénibles mais nécessaires:

```bash
make  # affiche l'aide
make help  # affiche l'aide
make format  # trie tes imports et formatte ton code
make lint  # évalue ton code
make test  # executer les tests (dans le dossier `tests`)
make format lint test  # faut les 3 d'affilés, s'arrête au 1er qui plante
```

Les `hooks/` sont des scripts executés avant chaque `git commit` et `git push` respectivement, pour s'assurer que le
code commité est bien formater par expl. Cf. `make setup-hooks`.
