"""
Implements a basic PokerHand object that encapsulates the cards that the hand
consists of, and a function to compare the value of the hand against other
hands.

"""
class PokerHand:
    def __init__(self, hand):
        try:
            # TODO check input format strictly, first character of each card
            # is the value, second is the suit
            self.hand = hand.split()

            if len(self.hand) != 5:
                raise ValueError("Invalid format: Hands must consist of "
                                 "exactly 5 cards.")

            self.score = self._calculate_score(self.hand)

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

    def _calculate_score(self):
        pass


class Result:
    WIN = 1
    LOSS = 2
    TIE = 3
