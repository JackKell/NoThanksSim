import random

from src.BaseNoThanksPlayer import BaseNoThanksPlayer


class RandomNoThanksPlayer(BaseNoThanksPlayer):
    def WillPass(self, boardState=None):
        return bool(random.getrandbits(1))
