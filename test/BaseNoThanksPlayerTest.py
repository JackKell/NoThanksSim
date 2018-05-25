import unittest
from nothankssim.BaseNoThanksPlayer import BaseNoThanksPlayer


class BaseNoThanksPlayerTest(unittest.TestCase):
    def test_GetScore1(self):
        player: BaseNoThanksPlayer = BaseNoThanksPlayer()
        player.tokens = 10
        player.cards = [20, 6]
        expectedScore = 16
        self.assertEqual(player.getCurrentScore(), expectedScore)

    def test_GetScore2(self):
        player: BaseNoThanksPlayer = BaseNoThanksPlayer()
        player.cards = [3, 4, 5, 6, 7, 8, 9]
        expectedScore = 3
        self.assertEqual(player.getCurrentScore(), expectedScore)

    def test_GetScore3(self):
        player: BaseNoThanksPlayer = BaseNoThanksPlayer()
        player.cards = [3, 35, 33, 34, 7, 8, 9]
        expectedScore = 43
        self.assertEqual(player.getCurrentScore(), expectedScore)

    def test_GetScore4(self):
        player: BaseNoThanksPlayer = BaseNoThanksPlayer()
        player.cards = [3, 4, 5, 7, 8, 9]
        expectedScore = 10
        self.assertEqual(player.getCurrentScore(), expectedScore)


if __name__ == '__main__':
    unittest.main()
