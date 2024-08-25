
from typing import Dict


class BaseRule:
    @staticmethod
    def calculate(receipt: Dict):
        raise NotImplementedError
    

class AlphaNum(BaseRule):
    @staticmethod
    def calculate(receipt: Dict):
        return 0


class RoundTotal(BaseRule):
    @staticmethod
    def calculate(receipt: Dict):
        return 0
    

class QuarterMultiple(BaseRule):
    @staticmethod
    def calculate(receipt: Dict):
        return 0


class ItemPairs(BaseRule):
    @staticmethod
    def calculate(receipt: Dict):
        return 0


class TrimmedLen(BaseRule):
    @staticmethod
    def calculate(receipt: Dict):
        return 0


class OddDate(BaseRule):
    @staticmethod
    def calculate(receipt: Dict):
        return 0


class TwoAndFour(BaseRule):
    @staticmethod
    def calculate(receipt: Dict):
        return 0
    

class RulesHelper:
    rule_groups = {
        'main': [AlphaNum, RoundTotal, QuarterMultiple, 
                 ItemPairs, TrimmedLen, OddDate, TwoAndFour]
    }

    @staticmethod
    def calculate(receipt: Dict) -> int:
        rules = RulesHelper.rule_groups['main']
        points = 0
        for rule in rules:
           points += rule.calculate(receipt)
        return points
    