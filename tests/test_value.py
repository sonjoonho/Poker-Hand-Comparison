from PokerHand.PokerHand import PokerHand, Value

import pytest

class TestValue:
    def test_royalflush(self):
        hand = PokerHand("10H JH QH KH AH")
        assert hand.value == Value.ROYAL_FLUSH

    def test_straightflush(self):
        hand = PokerHand("3C 4C 5C 6C 7C")
        assert hand.value == Value.STRAIGHT_FLUSH

    def test_fourofakind(self):
        hand = PokerHand("KC KH KD KS 5C")
        assert hand.value == Value.FOUR_OF_A_KIND

    def test_fullhouse(self):
        hand = PokerHand("KC KH KD 7C 7S")
        assert hand.value == Value.FULL_HOUSE

    def test_flush(self):
        hand = PokerHand("KC QC 9C 8C 2C")
        assert hand.value == Value.FLUSH

    def test_straight(self):
        hand = PokerHand("3C 4H 5D 6C 7C")
        assert hand.value == Value.STRAIGHT

    def test_threeofakind(self):
        hand = PokerHand("KC KH KD 7C 5S")
        assert hand.value == Value.THREE_OF_A_KIND

    def test_twopairs(self):
        hand = PokerHand("KC KH 7D 7C 5S")
        assert hand.value == Value.TWO_PAIRS

    def test_pair(self):
        hand = PokerHand("KC KH 7D 2C 5S")
        assert hand.value == Value.PAIR

    def test_pair(self):
        hand = PokerHand("AC 4H 7D KC 2S")
        assert hand.value == Value.HIGHCARD
