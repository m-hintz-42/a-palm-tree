from pip._internal import main
__author__ = 'mhintz'

packages = [
    "flask",
    "flask_sqlalchemy",
    "requests",
    "Frozen-Flask"
]


def install(package):
    for i in package:
        print ("\n" + i + " :")
        main(['install', i])

# Install necessary libraries
install(packages)