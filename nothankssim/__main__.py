from nothankssim.NoThanksGame import NoThanksGame
from nothankssim.RandomNoThanksPlayer import RandomNoThanksPlayer


def main():
    noThanksGame = NoThanksGame(startingTokens=11)

    playerA = RandomNoThanksPlayer(name="A")
    playerB = RandomNoThanksPlayer(name="B")
    playerC = RandomNoThanksPlayer(name="C")
    playerD = RandomNoThanksPlayer(name="D")

    noThanksGame.addPlayer(playerA)
    noThanksGame.addPlayer(playerB)
    noThanksGame.addPlayer(playerC)
    noThanksGame.addPlayer(playerD)

    noThanksGame.run()


if __name__ == '__main__':
    main()
