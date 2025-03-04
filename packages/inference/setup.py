from setuptools import setup

# Lire requirements.txt en filtrant les lignes vides et les commentaires
with open("requirements.txt") as f:
    requirements = [line.strip() for line in f.readlines() if line.strip() and not line.startswith("#")]

setup(
    name='kto-keras-inference',
    version='0.0.1',
    install_requires=requirements
)
