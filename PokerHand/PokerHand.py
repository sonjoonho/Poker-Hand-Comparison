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
        if self.value > other_hand.value:
            return Result.WIN
        elif self.value == other_hand.value:
            return Result.TIE
        else:
            return Result.LOSS


    def _calculate_value(self):
        """
        Calculates the value of a hand.

        Returns:
            The value of the hand, as a Value.
        """

        # First, define the ranks and their relative values.
        ranks = "AKQJT98765432"
        ranks_values = {'A': 12, 'K': 11, 'Q': 10, 'J': 9, 
                        'T': 8,  '9': 7 , '8': 6,  '7': 5, 
                        '6': 4,  '5': 3,  '4': 2,  '3': 1, '2': 0}

        # Calculate how many times a particular rank appears in the hand (if
        # at all) and store in a dict
        rank_counts_dict = {rank: "".join(self.cards).count(rank) for rank in ranks
                            if "".join(self.cards).count(rank) > 0}

        # Calculate present ranks, and sort according to their value as defined
        # by the map ranks_values above.
        present_ranks = sorted(rank_counts_dict.keys(), 
                               key=lambda k: ranks_values[k], reverse=True)

        # Store the counts of each rank sorted by frequency.
        rank_counts = sorted(list(rank_counts_dict.values()), reverse=True)

        # The hand is four of a kind if one rank appears 4 times, and another
        # appears once. A similar pattern of comparison is used below.
        if rank_counts == [4, 1]:
            return Value.FOUR_OF_A_KIND
        
        # The hand is a full house.
        if rank_counts == [3, 2]:
            return Value.FULL_HOUSE

        # The hand is three of a kind.
        if rank_counts == [3, 1, 1]:
            return Value.THREE_OF_A_KIND
        
        # The hand is a two pair.
        if rank_counts == [2, 2, 1]:
            return Value.TWO_PAIRS

        # The hand is a pair if one rank is repeated (so there are 4 distinct
        # cards).
        if len(present_ranks) == 4:
            return Value.PAIR

        # We have a flush if all the cards have the same suit.
        suits = [card[1] for card in self.cards]
        flush = suits.count(suits[0]) == len(suits)

        # Check if royal flush
        royal = sum([rank in ranks[:5] for rank in present_ranks]) == len(present_ranks)
        
        if royal and flush:
            return Value.ROYAL_FLUSH

        # We have a straight if the difference between the rank of the bottom
        # card and top card is 4. For this, we have the condition that every
        # card is distinct, hence the length check.
        # TODO check for wheel
        straight = False
        if len(present_ranks) == 5:
            straight = ranks_values[present_ranks[0]] - ranks_values[present_ranks[4]] == 4

        # If we have a straight and flush, we have a straight flush
        if straight and flush:
            return Value.STRAIGHT_FLUSH
        elif flush:
            return Value.FLUSH
        elif straight:
            return Value.STRAIGHT

        return Value.HIGHCARD


class Value:
    """
    Represents the value of a hand. Implemented as detailed by 
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
    """
    Represents the result of a poker hand comparison.
    """
    WIN = 1
    LOSS = 2
    TIE = 3
