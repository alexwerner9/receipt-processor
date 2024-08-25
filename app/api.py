from flasgger import Swagger
from flask import Blueprint, Flask
from receipts import receipts

app = Flask(__name__)
swagger = Swagger(app)


app.register_blueprint(receipts, url_prefix='/receipts')
