# -*- coding: utf-8 -*-
from flask import Flask
from flask_mail import Mail
from flask_mail import Message


# Sending Mail
class SendMail:
    def send_email(self,carListStr,email):
        app = Flask(__name__)
        app.config['MAIL_DEFAULT_SENDER'] = 'info@example.com'
        app.config['MAIL_SERVER']='sandbox.smtp.mailtrap.io'
        app.config['MAIL_PORT'] = 2525
        app.config['MAIL_USERNAME'] = '77b4c182dc8709'
        app.config['MAIL_PASSWORD'] = '86dc35b89d0708'
        app.config['AUTH'] = 'PLAIN'
        app.config['MAIL_USE_TLS'] = True
        app.config['MAIL_USE_SSL'] = False

        mail = Mail(app)

        with app.app_context():
            message = Message('Header', recipients=[email])
            message.body = str(carListStr)
            mail.send(message)