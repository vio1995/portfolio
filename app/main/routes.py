from flask import Blueprint, render_template, request, flash, redirect, url_for
from app.utilities.contact_form import Contact
from app.utilities.email import envia_Email
from app.utilities.recaptcha import verificar_recaptcha

import os

bp = Blueprint("main", __name__)

@bp.route("/")
def index():
    return render_template("index.html")

@bp.route("/about")
def about():
    return render_template("about.html")

@bp.route("/projects")
def projects():
    return render_template("projects.html")

@bp.route("/contact", methods=["GET", "POST"])
def contact():
    formulario = Contact()
    site_key = os.environ.get('RECAPTCHA_SITE_KEY')

    if formulario.validate_on_submit():
        recaptcha_response_token = request.form.get('g-recaptcha-response')
        if verificar_recaptcha(recaptcha_response_token):
            try:
                sucess, message_feedback = envia_Email(
                    name=formulario.name.data,
                    subject=formulario.subject.data,
                    sender=formulario.email.data,
                    msg=formulario.message.data)
                
                if sucess:
                    flash('✅ Mensagem enviada com sucesso! Retornarei o mais rápido possível.', 'success')
                else:
                    flash(message_feedback, 'danger')

                return redirect(url_for('main.contact'))

            except Exception as e:
                print(f"LOG - Erro: {e}")
                flash('❌ Opa! Ocorreu um problema interno.', 'danger')
        else:
            flash('Verificação "Não sou um robô" falhou. Por favor, tente novamente.', 'danger')

    return render_template("contact.html", formulario=formulario, site_key=site_key)
