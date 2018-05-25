import random

from nothankssim.BaseNoThanksPlayer import BaseNoThanksPlayer


class RandomNoThanksPlayer(BaseNoThanksPlayer):
    def willPass(self, boardState=None) -> bool:
        return bool(random.getrandbits(1))
