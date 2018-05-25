from abc import ABC, abstractclassmethod


class BaseNoThanksPlayer(ABC):
    def __init__(self, name=None):
        self.name = name
        self.tokens = 0
        self.cards = []

    def __str__(self):
        return str(self.name)

    @abstractclassmethod
    def willPass(self, boardState=None):
        return True

    def hasTokens(self):
        return self.tokens > 0

    def getCurrentScore(self):
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
