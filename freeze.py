from flask_frozen import Freezer
from palm_tree import tree

freezer = Freezer(tree)

if __name__ == '__main__':
    freezer.freeze()