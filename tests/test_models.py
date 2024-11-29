import functools
from pyclbr import Function
import random
import unittest
from app import db
from models import Aluno, Disciplina, Nota

class TestModels(unittest.TestCase):

    def test_relacao_aluno_disciplina(self):
        aluno = Aluno(nome='João Silva', matricula=123456)
        disciplina = Disciplina(nome='Matemática')
        aluno.disciplinas.append(disciplina)
        db.session.add(aluno)
        db.session.commit()

        aluno_db = Aluno.query.filter_by(nome='João Silva').first()
        self.assertEqual(len(aluno_db.disciplinas), 1)
        self.assertEqual(aluno_db.disciplinas[0].nome, 'Matemática')

    def test_consulta_complexa(self):
        aluno1 = Aluno(nome='João Silva', matricula=123456)
        aluno2 = Aluno(nome='Maria Santos', matricula=789012)
        disciplina1 = Disciplina(nome='Matemática')
        disciplina2 = Disciplina(nome='Português')
        nota1 = Nota(aluno=aluno1, disciplina=disciplina1, valor=8.5)
        nota2 = Nota(aluno=aluno1, disciplina=disciplina2, valor=9.0)
        nota3 = Nota(aluno=aluno2, disciplina=disciplina1, valor=7.0)
        db.session.add_all([aluno1, aluno2, disciplina1, disciplina2, nota1, nota2, nota3])
        db.session.commit()

        alunos_aprovados_em_matematica = Aluno.query.join(Nota).filter(
            Nota.disciplina_id == disciplina1.id,
            Function.avg(Nota.valor) > 8
        ).group_by(Aluno.id).all()

        self.assertEqual(len(alunos_aprovados_em_matematica), 1)
        self.assertEqual(alunos_aprovados_em_matematica[0].nome, 'João Silva')

    class TestModels(unittest.TestCase):

    def test_performance_consulta(self):
        for _ in range(1000):
            aluno = Aluno(nome=f'Aluno {_}', matricula=_ + 1)
            for _ in range(5):
                disciplina = Disciplina.query.order_by(db.func.random()).first()
                nota = Nota(aluno=aluno, disciplina=disciplina, valor=random.uniform(0, 10))
                db.session.add(nota)
            db.session.add(aluno)
        db.session.commit()

        start = time.time()
        alunos_excelentes = Aluno.query.join(Nota).group_by(Aluno.id).having(
            functools.avg(Nota.valor) > 8
        ).all()
        end = time.time()

        self.assertLess(end - start, 1, "Consulta demorou muito")

        import time
        start = time.time()
        end = time.time()
        self.assertLess(end - start, 1)
