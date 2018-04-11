from src.HumanNoThanksPlayer import HumanNoThanksPlayer
from src.NoThanksGame import NoThanksGame
from src.RandomNoThanksPlayer import RandomNoThanksPlayer


def main():
    # random.seed(123)
    noThanksGame = NoThanksGame()
    noThanksGame.AddPlayer(HumanNoThanksPlayer())
    noThanksGame.AddPlayer(RandomNoThanksPlayer())
    noThanksGame.AddPlayer(RandomNoThanksPlayer())
    noThanksGame.AddPlayer(RandomNoThanksPlayer())
    noThanksGame.AddPlayer(RandomNoThanksPlayer())
    noThanksGame.RunGame()


if __name__ == '__main__':
    main()
