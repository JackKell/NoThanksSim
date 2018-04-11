import random

from src.BaseNoThanksPlayer import BaseNoThanksPlayer


class NoThanksGame(object):
    def __init__(self):
        self.players = []
        self.deck = []
        self.discard = []
        self.card = None
        self.tokens = 0
        self.currentPlayerIndex = 0
        self.startingTokens = 10
        self.lowestCard = 3
        self.highestCard = 35
        self.totalDiscards = 4

    def AddPlayer(self, player):
        self.players.append(player)

    def NextPlayer(self):
        self.currentPlayerIndex += 1
        self.currentPlayerIndex %= len(self.players)

    def Pass(self, player):
        print("Player", self.currentPlayerIndex + 1, "Passes")
        player.tokens -= 1
        self.tokens += 1
        self.NextPlayer()

    def TakeCard(self, player):
        print("====> Player", self.currentPlayerIndex + 1, "Takes", self.card)
        player.tokens += self.tokens
        self.tokens = 0
        player.cards.append(self.card)
        self.Draw()

    def Draw(self):
        random.shuffle(self.deck)
        self.card = self.deck.pop()

    def PrintBoardInformation(self):
        print("Board Information")
        # Debug players should not see this information during game play
        # print("\tDiscard:", self.discard)
        # print("\tDeck:", self.deck)
        print("\tCard:", self.card)
        print("\tTokens:", self.tokens)
        print("\tCurrent Player:", self.currentPlayerIndex + 1)

    def PrintPlayerInformation(self):
        print("Player Information")
        for playerIndex, player in enumerate(self.players):
            print("\tPlayer", playerIndex + 1)
            print("\t\tTokens:", player.tokens)
            print("\t\tCards:", player.cards)
            print("\t\tScore:", player.GetScore())

    def PrintScoreBoard(self):
        print("Score Board")
        for playerIndex, player in enumerate(self.players):
            print("\tPlayer", playerIndex + 1, player.GetScore(), "points")

    def SetupGame(self):
        self.DealTokens()
        self.InitializeDeck()
        self.Draw()

    def DealTokens(self):
        for player in self.players:
            player.tokens = self.startingTokens

    def InitializeDeck(self):
        self.deck = list(range(self.lowestCard, self.highestCard + 1))
        random.shuffle(self.deck)
        self.discard = self.deck[:self.totalDiscards]
        self.deck = self.deck[self.totalDiscards:]

    def GetCurrentPlayer(self):
        return self.players[self.currentPlayerIndex]

    def PromptCurrentPlayer(self):
        currentPlayer: BaseNoThanksPlayer = self.GetCurrentPlayer()
        if currentPlayer.CanPass():
            if currentPlayer.WillPass():
                self.Pass(currentPlayer)
            else:
                self.TakeCard(currentPlayer)
        else:
            self.TakeCard(currentPlayer)

    def RunGame(self):
        self.SetupGame()
        while self.deck:
            self.PrintBoardInformation()
            self.PrintPlayerInformation()
            self.PromptCurrentPlayer()
            print()
        self.PrintScoreBoard()



