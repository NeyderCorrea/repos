import os
from flask import Flask

def create_app():
    app = Flask(__name__)

    app.config.from_mapping(
        FROM_MAIL=os.environ.get('FROM_MAIL'),
        MAIL_PASS=os.environ.get('MAIL_PASS'),
        SECRET_KEY=os.environ.get('SECRET_KEY')
    )

    from . import portfolio

    app.register_blueprint(portfolio.bp)

    return app