from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config

app = Flask(__name__)

config_name = os.getenv('FLASK_CONFIG', 'development')
app.config.from_object(config[config_name])

db = SQLAlchemy(app)

from models import Aluno, Disciplina, Nota
from routes import *

if __name__ == '__main__':
    app.run(debug=True)