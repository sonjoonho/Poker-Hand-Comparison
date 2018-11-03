#from .context import PokerHand
from PokerHand.PokerHand import PokerHand, Result

import pytest

class TestComparison:
    def test_one(self):
        # Pair
        HAND_ONE = PokerHand("AC 4S 5S 8C AH")
        # Pair
        HAND_TWO = PokerHand("4S 5S 8C AS AD")

        assert HAND_ONE.compareWith(HAND_TWO) == Result.TIE

    def test_two(self):
        # Flush
        HAND_ONE = PokerHand("KC QC 9C 8C 2C")
        # Pair
        HAND_TWO = PokerHand("4S 5S 8C AS AD")

        assert HAND_ONE.compareWith(HAND_TWO) == Result.WIN

    def test_three(self):
        # Pair
        HAND_ONE = PokerHand("7D 2C KH 5S KC")
        # Two pair
        HAND_TWO = PokerHand("7D 5C KD KH 7H")

        assert HAND_ONE.compareWith(HAND_TWO) == Result.LOSS
