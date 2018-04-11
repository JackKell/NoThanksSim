import random
from abc import ABC, abstractclassmethod


class BaseNoThanksPlayer(ABC):
    def __init__(self):
        self.tokens = 0
        self.cards = []

    @abstractclassmethod
    def WillPass(self, boardState=None):
        return True

    def CanPass(self):
        return self.tokens > 0

    def GetScore(self):
        score = self.tokens * -1
        if len(self.cards) != 0:
            self.cards.sort(reverse=True)
            score = self.cards[-1]
            for i in range(len(self.cards) - 1):
                card = self.cards[i]
                nextCard = self.cards[i + 1]
                if card != nextCard + 1:
                    score += card
            score -= self.tokens
        return score
