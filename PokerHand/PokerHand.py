"""
Implements a basic PokerHand object that encapsulates the cards that the hand
consists of, and a function to compare the value of the hand against other
hands.

"""
class PokerHand:
    def __init__(self, cards):
        try:
            # TODO check input format strictly, first character of each card
            # is the value, second is the suit
            self.cards = cards.split()

            if len(self.cards) != 5:
                raise ValueError("Invalid format: Hands must consist of "
                                 "exactly 5 cards.")

            self.value = self._calculate_value()

        except (AttributeError, TypeError):
            print("Invalid format: Hand must be a string.")


    def compareWith(self, other_hand):
        """
        Args:
            other_hand A PokerHand to be compared with.

        Returns:
            The result of the comparison.
        """

        return Result.TIE

    def _calculate_value(self):
        pass

class value:
    """
    Represents the value of a hand. Implemented according to as detailed by 
    https://en.wikipedia.org/wiki/Texas_hold_%27em#Hand_values. 
    """
    HIGHCARD = 0
    PAIR = 1
    TWO_PAIRS = 2
    THREE_OF_A_KIND = 3
    STRAIGHT = 4
    FLUSH = 5
    FULL_HOUSE = 6
    FOUR_OF_A_KIND = 7
    STRAIGHT_FLUSH = 8
    ROYAL_FLUSH = 9


class Result:
    WIN = 1
    LOSS = 2
    TIE = 3
