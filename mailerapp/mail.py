from crypt import methods
import smtplib
from re import search
import sendgrid
from sendgrid import *
from sendgrid.helpers.mail import *
from flask import (
    Blueprint, render_template, request, flash, url_for, redirect, current_app
)

from .db import get_db

bp = Blueprint('mail', __name__, url_prefix='/')

@bp.route('/', methods=['GET'])
def index():
    search = request.args.get('search')
    db, c = get_db()
    if search is None:
        c.execute("SELECT * FROM email")
    else:
        c.execute("SELECT * FROM email WHERE content like %s", ('%' + search + '%', ))
    
    mails = c.fetchall()

    return render_template('mails/index.html', mails=mails)

@bp.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        email = request.form.get('email')
        subject = request.form.get('subject')
        content = request.form.get('content')
        errors = []

        if not email:
            errors.append('¡Email es Obligatorio!')

        if not subject:
            errors.append('Asunto es Obligatorio!')

        if not content:
            errors.append('Conteido es Obligatorio!')

        if len(errors) == 0:
            send(email, subject, content)
            db, c = get_db()
            c.execute("INSERT INTO email (email, subject, content) VALUES (%s, %s, %s)", (email, subject, content))
            db.commit()

            return redirect(url_for('mail.index'))
        else:
            for error in errors:
                flash(error)

    return render_template('mails/create.html')

#def send(to, subject, content):
#    sg = sendgrid.SendGridAPIClient(api_key=current_app.config['SENDGRID_KEY'])
#    from_email = Email(current_app.config['FROM_EMAIL'])
#    to_email = To(to)
#    content = Content('text/plain', content)
#    mail = Mail(from_email, to_email, subject, content)
#    response = sg.client.mail.send.post(request_body=mail.get())

def send(to, subject, content):
    from_email = current_app.config['FROM_EMAIL']
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(from_email, current_app.config['MAIL_PASS'])
    server.sendmail(from_email, to, content)
    server.quit()