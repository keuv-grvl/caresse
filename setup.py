import codecs
import os

from setuptools import find_packages, setup


def read(rel_path):
    here = os.path.abspath(os.path.dirname(__file__))
    with codecs.open(os.path.join(here, rel_path), "r") as fp:
        return fp.read()


def get_version(rel_path):
    for line in read(rel_path).splitlines():
        if line.startswith("__version__"):
            delim = '"' if '"' in line else "'"
            return line.split(delim)[1]
    else:
        raise RuntimeError("Unable to find version string.")


with open("requirements.txt") as f:
    required = f.read().splitlines()

with open("ci-requirements.txt") as f:
    ci_required = f.read().splitlines()


setup(
    name="caresse",
    version=get_version("caresse/__init__.py"),  # <== ça va chercher la version dans le fichier
    description="Description du package",
    url="https://github.com/caresse-crew/caresse",
    author="Caresse corp.",
    author_email="your@email.net",
    packages=find_packages(),  # <== ça va chercher tous les sous-dossiers qui contiennet un `__init__.py`
    install_requires=required,  # <== deps nécessaire pour le package
    extras_require={"dev": ci_required},  # <== deps additionnelles, ici pour la phase de dev
    include_package_data=True,
    zip_safe=False,
)

# more info: https://docs.python.org/fr/3/distutils/setupscript.html
