from flask import Flask
from .model.database import createDatabase
app = Flask(__name__)


createDatabase().user()


from .view.index import homePage