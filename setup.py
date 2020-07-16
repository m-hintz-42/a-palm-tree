from pip._internal import main
__author__ = 'mhintz'

packages = [
    "flask==1.1.2",
    "flask_sqlalchemy==2.1",
    "requests==2.10.0"
]


def install(package):
    for i in package:
        print ("\n" + i + " :")
        main(['install', i])

# Install necessary libraries
install(packages)