from collections import defaultdict

"""
Implements a basic PokerHand object that encapsulates the cards that the hand
consists of, and a function to compare the value of the hand against other
hands.

"""
class PokerHand:
    def __init__(self, cards):
          # TODO check input format strictly, first character of each card
          # is the value, second is the suit
        cards.upper() 

        self.cards = cards.split()

        if len(self.cards) != 5:
            raise ValueError("Invalid format: Hands must consist of "
                             "exactly 5 cards.")

        self.value = self._calculate_value()


    def compareWith(self, other_hand):
        """
        Args:
            other_hand A PokerHand to be compared with.

        Returns:
            The result of the comparison.
        """

        return Result.TIE

    def _calculate_value(self):
        """
        Calculates the value of a hand.

        Returns:
            The value of the hand, as a Value.
        """
        
        # Calculate the frequency of each rank (ignoring suits) and sort
        ranks = "AKQJT98765432"
        # TODO can be done more succinctly
        # Store the joined string version of the cards as this can be easier to
        # work with sometimes
        cards_joined = "".join(self.cards)
        rank_counts_dict = {rank: cards_joined.count(rank) for rank in ranks}
        rank_counts = sorted(list(rank_counts_dict.values()), reverse=True)

        print(self.cards)
        print(rank_counts)

        # The hand is four of a kind
        if rank_counts[:2] == [4, 1]:
            return Value.FOUR_OF_A_KIND
        
        # The hand is a full house
        if rank_counts[:2] == [3, 2]:
            return Value.FULL_HOUSE

        # The hand is three of a kind
        if rank_counts[:3] == [3, 1, 1]:
            return Value.THREE_OF_A_KIND
        
        # The hand is a two pair
        if rank_counts[:3] == [2, 2, 1]:
            return Value.TWO_PAIRS

        # The hand is a pair
        if sum(count > 0 for count in rank_counts) == 4:
            return Value.PAIR

        # We have a flush if all the cards have the same suit = All cards 
        # have the same suit as the first card
        # This implementation is somewhat esoteric, but very fast.
        flush = cards_joined.count(self.cards[0][1]) == len(cards_joined)

        # We have a straight if the difference between the rank of the bottom
        # card and top card is 4.
        # TODO Finish this implementation
        # straight = 

        # If we have a straight and flush, we have a straight flush

        return Value.HIGHCARD
    

class Value:
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
