from flask import Flask
from flask_moment import Moment


app = Flask(__name__)
moment = Moment(app)  # подключаю библиотеку к приложению

from routes import *

if __name__ == '__main__':
    app.run()
