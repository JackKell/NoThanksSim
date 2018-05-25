import random

from nothankssim.BaseNoThanksPlayer import BaseNoThanksPlayer


class RandomNoThanksPlayer(BaseNoThanksPlayer):
    def willPass(self, boardState=None):
        return bool(random.getrandbits(1))
