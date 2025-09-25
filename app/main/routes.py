from flask import Blueprint, render_template, request, flash, redirect, url_for
from app.utilities.contact_form import Contact
from app.utilities.email import envia_Email

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

    if formulario.validate_on_submit():
        try:
            sucess, message_feedback = envia_Email(
                name=formulario.name.data,
                subject=formulario.subject.data,
                sender=formulario.email.data,
                message=formulario.message.data)

            if sucess:
                flash('✅ Mensagem enviada com sucesso! Retornarei o mais rápido possível.', 'success')
            else:
                flash(message_feedback, 'danger')

            return redirect(url_for('main.contact'))

        except Exception as e:
            print(f"LOG - Erro: {e}")
            flash('❌ Opa! Ocorreu um problema interno.', 'danger')

    return render_template("contact.html", formulario=formulario)
