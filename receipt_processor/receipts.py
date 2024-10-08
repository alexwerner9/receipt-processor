"""Route handling for the /receipts endpoints."""
import os
from uuid import uuid4

from flasgger import swag_from
from flask import Blueprint, Flask, Response, request

from receipt_processor.database import database_receipts
from receipt_processor.helpers import documentation_file
from receipt_processor.rules import RulesHelper

receipts = Blueprint('receipts', __name__)

@receipts.route('/process', methods=['POST'])
@swag_from(documentation_file('receipts', 'process.yml'))
def process():
    """Takes in a JSON receipt and returns a JSON object with an ID."""
    receipt = request.get_json(silent=True)
    if not receipt:
        return Response(response="JSON was invalid", status=400)
    
    receipt_id = str(uuid4())
    database_receipts[receipt_id] = receipt
    return {'id': receipt_id}


@receipts.route('/<id>/points', methods=['GET'])
@swag_from(documentation_file('receipts', 'points.yml'))
def points(id):
    """Takes a receipt ID and returns the points."""
    receipt = database_receipts.get(id)
    if not receipt:
        return Response(response=f"No receipt with id {id} found.", status=404)
    
    points = RulesHelper.calculate(receipt)
    return {'points': points}
