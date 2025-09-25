from flask import current_app
from flask_mail import Message
from app import mail

def envia_Email(name, subject, sender, message):
    try:
        destinatario = current_app.config['MAIL_RECIPIENT']
        msg = Message(subject, recipients=[destinatario])
        msg.body = f'De: {name} <{sender}> \n\n {message}'
        mail.send(msg)

        return True, 'Mensagem enviada com sucesso!'
    except Exception as e:
        print(f'LOG - Erro: {e}')
        return False, f'Ocorreu um erro ao enviar a mensagem: {e}'