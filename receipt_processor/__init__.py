"""Flask app factory."""
from flasgger import Swagger
from flask import Flask

import config


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config.ProdConfig)
    Swagger(app)

    with app.app_context():
        from receipt_processor import receipts
        app.register_blueprint(receipts.receipts, url_prefix='/receipts')
        return app
