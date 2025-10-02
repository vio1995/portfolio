from flask import current_app
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail


def envia_Email(name, subject, sender, msg):
    remetente = os.environ.get('MAIL_DEFAULT_SENDER')
    destinatario = os.environ.get('MAIL_RECIPIENT')
    api_key = os.environ.get('SENDGRID_API_KEY')

    html_content = f"""
        <h3>Nova mensagem de contato recebida</h3>
        <p><strong>De:</strong> {name} <{sender}></p>
        <p><strong>Assunto:</strong> {subject}</p>
        <hr>
        <p>{msg.replace('\n', '<br>')}</p>
    """

    message = Mail(
        from_email = remetente,
        to_emails=destinatario,
        subject=subject,
        html_content=html_content
    )

    try:
        sg = SendGridAPIClient(api_key)
        response = sg.send(message)

        print(f'Email enviado para {destinatario}, status code: {response.status_code}')

        return True, 'Mensagem enviada com sucesso!'
    except Exception as e:
        print(f'LOG - Erro: {e}')

        return False, f'Ocorreu um erro ao enviar a mensagem: {e}'