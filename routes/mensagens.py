# IMPORTAÇÕES NECESSÁRIAS

from flask import Blueprint, flash, request, redirect, url_for, render_template

# IMPORTAÇÕES PARA O ENVIO DE EMAIL

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

# IMPORTAR O " os " PARA REALIZAR ALGUMAS OPERAÇÕES

import os

# REGISTRO DO BLUEPRINT

email_bp = Blueprint("email", __name__)



# DIRETÓRIO DE UPLOAD PARA ENVIAR ANEXO

UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

def envio_email(destinatario, assunto, mensagem, caminho_anexo=None):
    
    
    # SERVIDOR PARA CONFIGURAÇÃO DE EMAIL
    SERVIDOR = 'smtp.gmail.com'
    PORTA = 587

    # CRIEI UM EMAIL PARA O PET SHOP SOMENTE PARA ENVIO DE MENSAGENS
    email_envio = 'melhoramigopetshop393@gmail.com'
    
    # CONFIGUREI NO GMAIL UM APP ESPECÍFICO QUE GERA UM TOKEN PARA ENVIO DE MENSAGENS DE APPS TERCEIROS
    
    email_senha = 'emtf ekdf ppia ybph'  

    # CONFIGURAÇÃO DA MENSAGEM
    msg = MIMEMultipart()
    msg['From'] = email_envio
    msg['To'] = destinatario
    msg['Subject'] = assunto

    msg.attach(MIMEText(mensagem, 'plain'))
    
    # CAMINHO PARA O ANEXO

    if caminho_anexo and os.path.isfile(caminho_anexo):

        with open(caminho_anexo, 'rb') as anexo:
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(anexo.read())
            encoders.encode_base64(part)
            part.add_header(
                'Content-Disposition',
                f'attachment; filename={os.path.basename(caminho_anexo)}'
            )
            msg.attach(part)
    else:
        print('Nenhum anexo foi encontrado ou o caminho é inválido')

    # ENVIANDO O EMAIL
    try:
        with smtplib.SMTP(SERVIDOR, PORTA) as servidor:
            servidor.starttls()
            servidor.login(email_envio, email_senha)
            servidor.sendmail(email_envio, destinatario, msg.as_string())
        flash('Mensagem enviada com sucesso!', category= 'success')
    except Exception as e:
        flash(f'Erro ao enviar mensagem: {str(e)}', category= 'error')

@email_bp.route('/contato/enviar', methods=['POST'])
def enviar_mensagem():
    
    # UTILIZEI UM EMAIL TEMPORARIO PARA TESTES
    
    # https://temp-mail.org/pt/
    
    # PODE GERAR UM NOVO EMAIL TEMPORARIO NO LINK ACIMA E COLOCAR NO CAMPO DESTINATÁRIO 
    destinatario = 'tihehe3007@hostlace.com'
    nome = request.form.get('nome')
    email = request.form.get('email')
    descricao = request.form.get('descricao')
    anexo = request.files.get('arquivo')

    if not nome or not email or not descricao:
        flash('Todos os campos são obrigatórios.')
        return redirect(url_for('email.index'))

    assunto = f"Mensagem de {nome} ({email})"
    mensagem = descricao

    if anexo and anexo.filename:
        caminho_anexo = os.path.join(UPLOAD_FOLDER, anexo.filename)
        anexo.save(caminho_anexo)
        envio_email(destinatario, assunto, mensagem, caminho_anexo)
    else:
        envio_email(destinatario, assunto, mensagem)

    return redirect(url_for('email.index'))

# PAGINA DO FORMULÁRIO DE CONTATO

@email_bp.route('/contato')
def index():
    return render_template('melhoramigo/main/contato/contato.html')








    
    



