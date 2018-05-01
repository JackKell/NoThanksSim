import random

from src.BaseNoThanksPlayer import BaseNoThanksPlayer
from src.NoThanksGame import NoThanksGame


class RatioNoThanksPlayer(BaseNoThanksPlayer):
    def WillPass(self, boardState: NoThanksGame = None):
        currentTokenToPointRatio = boardState.tokens / boardState.card
        if currentTokenToPointRatio >= .33:
            return bool(random.getrandbits(1))
        else:
            return True
