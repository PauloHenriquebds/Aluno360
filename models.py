from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Aluno(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    matricula = db.Column(db.String(10), unique=True, nullable=False)
    nome = db.Column(db.String(100), nullable=False)
    data_nascimento = db.Column(db.Date)
    notas = db.relationship('Nota', backref='aluno')

class Disciplina(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    codigo = db.Column(db.String(10), unique=True, nullable=False)
    nome = db.Column(db.String(100), nullable=False)
    notas = db.relationship('Nota', backref='disciplina')

class Nota(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    aluno_id = db.Column(db.Integer, db.ForeignKey('aluno.id'))
    disciplina_id = db.Column(db.Integer, db.ForeignKey('disciplina.id'))
    valor = db.Column(db.Float)