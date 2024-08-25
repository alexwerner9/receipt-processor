from flask import Blueprint, Flask, request, Response

receipts = Blueprint('receipts', __name__)

@receipts.route('/process', methods=['POST'])
def process():
    return ''


@receipts.route('/<id>/points', methods=['GET'])
def points(id):
    return ''

