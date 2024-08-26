"""Tests for the /receipts endpoints."""
from typing import Dict

import pytest
from flask.testing import FlaskClient
from pytest import FixtureRequest


class TestReceipts:
    def post_and_get_id(self, client: 'FlaskClient', receipt: Dict) -> str:
        response = client.post('/receipts/process', json=receipt)
        return response.json['id']

    @pytest.mark.parametrize('receipt_name', 
                             ['target_receipt', 'corner_market_receipt', 
                              'walgreens_receipt', 'simple_receipt'])
    def test_process_succeeds(self, client: 'FlaskClient', receipt_name: str, request: 'FixtureRequest') -> None:
        receipt = request.getfixturevalue(receipt_name)
        response = client.post('/receipts/process', json=receipt)
        assert response.status_code == 200
        assert 'id' in response.json

    def test_process_fails_get(self, client: 'FlaskClient') -> None:
        response = client.get('/receipts/process')
        assert response.status_code == 405

    def test_process_fails_post_no_json(self, client: 'FlaskClient') -> None:
        response = client.post('/receipts/process', data='123')
        assert response.status_code == 400
        assert 'JSON was invalid' in response.text

    @pytest.mark.parametrize('receipt_name,expected', 
                             [('target_receipt', 28), ('corner_market_receipt', 109), 
                              ('walgreens_receipt', 15), ('simple_receipt', 31)])
    def test_points(self, client: 'FlaskClient', receipt_name: str, expected: int, request: 'FixtureRequest') -> None:
        receipt = request.getfixturevalue(receipt_name)
        receipt_id = self.post_and_get_id(client, receipt)
        response = client.get(f'receipts/{receipt_id}/points')
        assert response.status_code == 200
        assert 'points' in response.json
        assert response.json['points'] == expected
