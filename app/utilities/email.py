from flask import current_app
from flask_mail import Message
from app import mail

def envia_Email(name, subject, sender, message):
    try:
        sender_username = current_app.config['MAIL_USERNAME']
        destinatario = current_app.config['MAIL_RECIPIENT']
        msg = Message(subject, sender=sender_username, recipients=[destinatario])
        msg.body = f'De: {name} <{sender}> \n\n {message}'
        mail.send(msg)

        return True, 'Mensagem enviada com sucesso!'
    except Exception as e:
        print(f'LOG - Erro: {e}')
        return False, f'Ocorreu um erro ao enviar a mensagem: {e}'