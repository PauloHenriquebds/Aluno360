import datetime

def formata_data(data):
    """Formata uma data para o formato 'DD/MM/YYYY'."""
    if isinstance(data, datetime.date):
        return data.strftime('%d/%m/%Y')
    else:
        return None

def valida_cpf(cpf):

    cpf = ''.join(c for c in cpf if c.isdigit())

    if len(cpf) != 11:
        return False

    try:
        int(cpf) 
    except ValueError:
        return False

    soma = 0
    for i in range(9):
        soma += int(cpf[i]) * (10 - i)
    resto = soma % 11
    if resto < 2:
        digito1 = 0
    else:
        digito1 = 11 - resto

    soma = 0
    for i in range(10):
        soma += int(cpf[i]) * (11 - i)
    resto = soma % 11
    if resto < 2:
        digito2 = 0
    else:
        digito2 = 11 - resto

    if digito1 != int(cpf[9]) or digito2 != int(cpf[10]):
        return False

    return True

def calcula_media(notas):

    if not notas:
        return None 

    return sum(notas) / len(notas)

import smtplib
from email.mime.text import MIMEText

def envia_email(destinatario, assunto, mensagem):

    host = 'smtp.gmail.com'
    port = 587
    username = 'seu_email@gmail.com'
    password = 'sua_senha'

    msg = MIMEText(mensagem)
    msg['From'] = username
    msg['To'] = destinatario
    msg['Subject'] = assunto

    with smtplib.SMTP(host, port) as smtp:
        smtp.starttls()
        smtp.login(username, password)
        smtp.sendmail(username, destinatario, msg.as_string())

from fpdf import FPDF # type: ignore

def gera_relatorio_alunos(alunos):

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.cell(40, 10, 'Nome', 1, 0, 'L')
    pdf.cell(40, 10, 'Matrícula', 1, 0, 'L')
    pdf.cell(20, 10, 'Nota 1', 1, 0, 'L')
    pdf.cell(20, 10, 'Nota 2', 1, 1, 'L')

    for aluno in alunos:
        pdf.cell(40, 10, aluno['nome'], 1, 0, 'L')
        pdf.cell(40, 10, aluno['matricula'], 1, 0, 'L')
        pdf.cell(20, 10, str(aluno['notas'][0]), 1, 0, 'L')
        pdf.cell(20, 10, str(aluno['notas'][1]), 1, 1, 'L')

    pdf.output('relatorio_alunos.pdf')
