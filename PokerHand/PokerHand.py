def hi(s):
    print("hello")
class PokerHand:
    def __init__(self, hand):
        self.hand = hand

    def compareWith(self, other_hand):

        return Result.TIE

class Result:
    WIN = 1
    LOSS = 2
    TIE = 3
