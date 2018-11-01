#from .context import PokerHand
from PokerHand.PokerHand import PokerHand, Result

import pytest

class TestBasic:
    def test_one(self):
        HAND_ONE = PokerHand("AC 4S 5S 8C AH")
        HAND_TWO = PokerHand("4S 5S 8C AS AD")

        assert HAND_ONE.compareWith(HAND_TWO) == Result.TIE

