from abc import ABC, abstractclassmethod
from typing import List


class BaseNoThanksPlayer(ABC):
    def __init__(self):
        self.tokens: int = 0
        self.cards: List[int] = []

    @abstractclassmethod
    def WillPass(self, boardState=None) -> bool:
        pass

    def CanPass(self) -> bool:
        return self.tokens > 0

    def GetScore(self) -> int:
        score: int = 0
        if self.cards:
            lastCardIndex: int = len(self.cards) - 1
            sortedCards: List[int] = sorted(self.cards, reverse=True)
            for cardIndex, card in enumerate(sortedCards):  # type: int, int
                if cardIndex == lastCardIndex:
                    score += card
                else:
                    nextCard: int = sortedCards[cardIndex + 1]
                    if (card - 1) != nextCard:
                        score += card
        score -= self.tokens
        return score
