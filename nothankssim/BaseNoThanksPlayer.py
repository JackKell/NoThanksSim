from abc import ABC, abstractclassmethod
from typing import List


class BaseNoThanksPlayer(ABC):
    def __init__(self, name=None):
        self.name: str = name
        self.tokens: int = 0
        self.cards: List[int] = []

    def __str__(self):
        return str(self.name)

    @abstractclassmethod
    def willPass(self, boardState=None) -> bool:
        return True

    def hasTokens(self) -> bool:
        return self.tokens > 0

    def getCurrentScore(self) -> int:
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

    def passCard(self):
        self.tokens -= 1
        if self.tokens < 0:
            raise ValueError(self.tokens, "must not go below 0")

    def takeCard(self, card, tokens):
        self.tokens += tokens
        self.cards.append(card)

    def reset(self):
        self.tokens = 0
        self.cards = []
