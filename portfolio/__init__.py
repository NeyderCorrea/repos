import os
from flask import Flask

def create_app():
    app = Flask(__name__)

    app.config.from_mapping(
        SENDGRID_KEY=os.environ.get('SENDGRID_API_KEY'),
        FROM_MAIL=os.environ.get('FROM_MAIL'),
        MAIL_PASS=os.environ.get('MAIL_PASS'),
        SECRET_KEY=os.environ.get('SECRET_KEY'),
        DATABASE_HOST=os.environ.get('FLASK_DATABASE_HOST'),
        DATABASE_USER=os.environ.get('FLASK_DATABASE_USER'),
        DATABASE_PASSWORD=os.environ.get('FLASK_DATABASE_PASSWORD'),
        DATABASE=os.environ.get('FLASK_DATABASE')
    )

    from . import portfolio

    app.register_blueprint(portfolio.bp)

    return app