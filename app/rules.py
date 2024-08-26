"""All rules. If desired, these can be split into separate files in the future."""
import math
from typing import Dict


class BaseRule:
    """Base rule class. All children must implement calculate function."""
    @staticmethod
    def calculate(receipt: Dict):
        raise NotImplementedError
    

class AlphaNum(BaseRule):
    """Points = number of alphanumeric characters in retailer name."""
    @staticmethod
    def calculate(receipt: Dict):
        retailer_name = receipt.get('retailer', '')
        return len([char for char in retailer_name if char.isalnum()])


class RoundTotal(BaseRule):
    """Points = 50 if total is a round dollar amount, 0 otherwise."""
    @staticmethod
    def calculate(receipt: Dict):
        total = float(receipt.get('total', 0))
        if total == int(total):
            return 50
        return 0
    

class QuarterMultiple(BaseRule):
    """Points = 25 if total is a multiple of 25."""
    @staticmethod
    def calculate(receipt: Dict):
        total = float(receipt.get('total', 0))
        if total % 0.25:
            return 0
        return 25


class ItemPairs(BaseRule):
    """Points = 5 points for every two items on receipt."""
    @staticmethod
    def calculate(receipt: Dict):
        items = receipt.get('items', [])
        num_items = len(items)
        return 5 * (num_items // 2)


class TrimmedLen(BaseRule):
    """Points = If the trimmed length of the item description is a multiple of 3, 
    multiply the price by 0.2 and round up to the nearest integer."""
    @staticmethod
    def calculate(receipt: Dict):
        points = 0
        for item in receipt.get('items'):
            description = item.get('shortDescription').strip()
            price = float(item.get('price'))
            if not len(description) % 3:
                price *= 0.2
                points += math.ceil(price)
        return points


class OddDate(BaseRule):
    """Points = 6 points if the day in the purchase date is odd."""
    @staticmethod
    def calculate(receipt: Dict):
        purchase_date = receipt.get('purchaseDate', '0-0-0')
        date = int(purchase_date.split('-')[2])
        if date % 2:
            return 6
        return 0


class TwoAndFour(BaseRule):
    """Points = 10 points if between 2pm and 4pm."""
    @staticmethod
    def calculate(receipt: Dict):
        purchase_time = receipt.get('purchaseTime', '00:00')
        if purchase_time > '14:00' and purchase_time < '16:00':
            return 10
        return 0
    

class RulesHelper:
    rule_groups = {
        'main': [AlphaNum, RoundTotal, QuarterMultiple, 
                 ItemPairs, TrimmedLen, OddDate, TwoAndFour]
    }

    @staticmethod
    def calculate(receipt: Dict) -> int:
        """Calculate the number of points based on receipt.

        Args:
            receipt (Dict): the receipt to calculate points for

        Returns:
            int: the number of points
        """
        # in case we want to handle different receipts with different rules
        # in the future
        rules = RulesHelper.rule_groups['main']
        points = 0
        for rule in rules:
           points += rule.calculate(receipt)
        return points
    