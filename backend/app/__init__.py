from flask import Flask
from flask_script import Manager
from flask_cors import CORS
import os


app = Flask(__name__)

CORS(app)

manager = Manager(app)

for i in ['controllers', 'classes']:
    classes = {}
    IMPORT_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), i)

    to_import = [name for name in os.listdir(
        IMPORT_PATH) if os.path.isdir(os.path.join(IMPORT_PATH, name))]

    for x in to_import:
        classes[x] = __import__('app.{0}.'.format(i) + x, fromlist=['*'])
        
