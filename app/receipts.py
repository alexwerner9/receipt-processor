from uuid import uuid4

from database import database_receipts
from flask import Blueprint, Flask, Response, request
from rules import RulesHelper

receipts = Blueprint('receipts', __name__)

@receipts.route('/process', methods=['POST'])
def process():
    """Takes in a JSON receipt and returns a JSON object with an ID.
    ---
    parameters:
        - name: body
          in: body
          required: true
    responses:
        200:
            description: A JSON object with an ID to be used in /receipts/<id>/points
            schema:
                type: object
                properties:
                    id:
                        type: string
    """
    receipt = request.get_json(silent=True)
    if not receipt:
        return Response(response="JSON was invalid", status=400)
    
    receipt_id = str(uuid4())
    database_receipts[receipt_id] = receipt
    print(database_receipts)
    return {'id': receipt_id}


@receipts.route('/<id>/points', methods=['GET'])
def points(id):
    """Takes a receipt ID and returns the points.
    ---
    parameters:
        - name: id
          in: path
          type: string
          required: true
    responses:
        200:
            description: a JSON with the points
            schema:
                type: object
                properties:
                    points:
                        type: string
    """
    print(database_receipts)
    receipt = database_receipts.get(id)
    if not receipt:
        return Response(response=f"No receipt with id {id} found.", status=404)
    
    points = RulesHelper.calculate(receipt)
    return {'points': points}

