from src.HumanNoThanksPlayer import HumanNoThanksPlayer
from src.NoThanksGame import NoThanksGame
from src.RandomNoThanksPlayer import RandomNoThanksPlayer
from src.RatioNoThanksPlayer import RatioNoThanksPlayer


def main():
    # random.seed(123)
    noThanksGame = NoThanksGame()
    noThanksGame.AddPlayer(HumanNoThanksPlayer())
    noThanksGame.AddPlayer(RatioNoThanksPlayer())
    noThanksGame.AddPlayer(RatioNoThanksPlayer())
    noThanksGame.AddPlayer(RatioNoThanksPlayer())
    noThanksGame.RunGame()


if __name__ == '__main__':
    main()
