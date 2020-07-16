from flask import Flask
from flask_sqlalchemy import SQLAlchemy

tree = Flask(__name__, static_url_path='/static')
# tree.config.from_object('config')
# db = SQLAlchemy(tree)

import palm_tree.coconut_1.controller_1

