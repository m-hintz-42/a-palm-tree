from flask import render_template
from palm_tree import tree

__author__ = 'mhintz'
tree.secret_key = 'dawg'


@tree.route('/')
def generate_home(name=None):
    return render_template('base.html', name=name)


@tree.route('/home/')
def home():
    return render_template('data.html')


@tree.route('/home/coco')
def dance():
    return render_template('coco.html')
