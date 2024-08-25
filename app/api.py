from flask import Blueprint, Flask
from receipts import receipts
app = Flask(__name__)

app.register_blueprint(receipts, url_prefix='/receipts')
