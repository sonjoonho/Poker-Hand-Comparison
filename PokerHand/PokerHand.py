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
        ranks_values = {'A': 12, 'K': 11, 'Q': 10, 'J': 9, 
                        'T': 8,  '9': 7 , '8': 6,  '7': 5, 
                        '6': 4,  '5': 3,  '4': 2,  '3': 1, '2': 0}

        # TODO can be done more succinctly
        # Store the joined string version of the cards as this can be easier to
        # work with sometimes
        # FIXME is this even used?
        cards_joined = "".join(self.cards)
        rank_counts_dict = {rank: cards_joined.count(rank) for rank in ranks}

        # Calculate present ranks, and sort according to their value
        # This is used in calculating whether of not all the cards are royal,
        # and calculating if the hand is a straight.
        present_ranks = [r for (r, c) in rank_counts_dict.items() if c > 0]
        present_ranks = sorted(present_ranks, key=lambda k: ranks_values[k], 
                               reverse=True)


        rank_counts = sorted(list(rank_counts_dict.values()), reverse=True)

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
        if len(present_ranks) == 4:
            return Value.PAIR

        # We have a flush if all the cards have the same suit = All cards 
        # have the same suit as the first card
        # This implementation is somewhat esoteric, but very fast.
        suits = [card[1] for card in self.cards]
        flush = suits.count(suits[0]) == len(suits)


        # Check if royal flush
        royal = sum([(rank in ranks[:5]) for rank in present_ranks]) == len(present_ranks)
        
        if royal and flush:
            return Value.ROYAL_FLUSH

        print(self.cards)
        print(present_ranks)
        print(rank_counts)

        # We have a straight if the difference between the rank of the bottom
        # card and top card is 4.
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
