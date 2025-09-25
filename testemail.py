# teste_flask_app.py
import os
from flask import Flask, render_template_string, request, flash
from flask_mail import Mail, Message
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email

# --- CONFIGURAÇÃO DIRETA NO CÓDIGO ---
app = Flask(__name__)
app.config['SECRET_KEY'] = 'coloque-sua-secret-key-aqui' # Substitua
app.config['TESTING'] = True

# Configuração do SendGrid
app.config['MAIL_SERVER'] = 'smtp.sendgrid.net'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = 'apikey' # Substitua
app.config['MAIL_PASSWORD'] = 'SG.xxxxxxxxxxxxxxxx' # Substitua com sua chave de API
app.config['MAIL_DEFAULT_SENDER'] = 'seu-email-verificado-no-sendgrid@exemplo.com' # Substitua

MAIL_RECIPIENT = 'seu-email-de-destino@exemplo.com' # Substitua

mail = Mail(app)

# --- FORMULÁRIO WTForms ---
class ContatoSimplesForm(FlaskForm):
    nome = StringField('Nome', validators=[DataRequired()])
    submit = SubmitField('Enviar Teste')

# --- TEMPLATE HTML ---
HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head><title>Teste Final</title></head>
<body>
    <h1>Teste Final de Envio</h1>
    {% with messages = get_flashed_messages() %}
        {% if messages %}
            <ul style="color: green; font-weight: bold;">
            {% for message in messages %}
                <li>{{ message }}</li>
            {% endfor %}
            </ul>
        {% endif %}
    {% endwith %}
    <form method="POST">
        {{ form.hidden_tag() }}
        {{ form.nome.label }} {{ form.nome() }}
        {{ form.submit() }}
    </form>
</body>
</html>
"""

# --- ROTA FLASK ---
@app.route('/', methods=['GET', 'POST'])
def index():
    form = ContatoSimplesForm()
    if form.validate_on_submit():
        try:
            print("--- TENTANDO ENVIAR EMAIL PELO FLASK-MAIL ---")
            msg = Message(
                subject="Teste de Sucesso do Flask-Mail!",
                recipients=[MAIL_RECIPIENT]
            )
            msg.body = f"E-mail de teste enviado por {form.nome.data}."
            mail.send(msg)
            flash("E-MAIL ENVIADO COM SUCESSO!")
            print("--- SUCESSO! ---")
        except Exception as e:
            print("--- ERRO NO ENVIO DO FLASK-MAIL ---")
            print(e)
            flash(f"ERRO: {e}")
    return render_template_string(HTML_TEMPLATE, form=form)

# --- EXECUTAR O APP ---
if __name__ == '__main__':
    app.run(debug=True, port=5001) # Usando a porta 5001 para não conflitar