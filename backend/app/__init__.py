from flask import Flask
from flask_script import Manager
from flask_cors import CORS
import os


app = Flask(__name__)
app.config.from_object('config')

CORS(app)

manager = Manager(app)

for i in ['classes', 'controllers']:
    modules = {}
    IMPORT_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), i)

    to_import = [name for name in os.listdir(
        IMPORT_PATH) if os.path.isdir(os.path.join(IMPORT_PATH, name))]

    for x in to_import:
        modules[x] = __import__('app.{0}.'.format(i) + x, fromlist=['*'])
        
