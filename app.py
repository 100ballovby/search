from flask import Flask
from flask_moment import Moment
from flask_bootstrap import Bootstrap


app = Flask(__name__)
moment = Moment(app)  # подключаю библиотеку к приложению
bootstrap = Bootstrap(app)  # подключаю бутстрап к приложению
app.config['SECRET_KEY'] = 'hard to guess'

from routes import *

if __name__ == '__main__':
    app.run()
