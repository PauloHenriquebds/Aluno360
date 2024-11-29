from flask import render_template, request, redirect, url_for
from app import app, db
from models import Aluno, Disciplina, Nota

@app.route('/')
def home():
    alunos = Aluno.query.all()
    return render_template('index.html', alunos=alunos)

@app.route('/aluno/<int:aluno_id>')
def aluno_detalhes(aluno_id):
    aluno = Aluno.query.get_or_404(aluno_id)
    return render_template('aluno.html', aluno=aluno)

@app.route('/aluno/novo', methods=['GET', 'POST'])
def novo_aluno():
    if request.method == 'POST':
        novo_aluno = Aluno(matricula=request.form['matricula'],
                           nome=request.form['nome'],
                           data_nascimento=request.form['data_nascimento'])
        db.session.add(novo_aluno)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('novo_aluno.html')

@app.route('/aluno/editar/<int:aluno_id>', methods=['GET', 'POST'])
def editar_aluno(aluno_id):
    aluno = Aluno.query.get_or_404(aluno_id)
    if request.method == 'POST':
        aluno.matricula = request.form['matricula']
        aluno.nome = request.form['nome']
        aluno.data_nascimento = request.form['data_nascimento']
        db.session.commit()
        return redirect(url_for('aluno_detalhes', aluno_id=aluno.id))
    return render_template('editar_aluno.html', aluno=aluno)

@app.route('/aluno/excluir/<int:aluno_id>', methods=['POST'])
def excluir_aluno(aluno_id):
    aluno = Aluno.query.get_or_404(aluno_id)
    db.session.delete(aluno)
    db.session.commit()
    return redirect(url_for('home'))