import random
from typing import List

from src.BaseNoThanksPlayer import BaseNoThanksPlayer


class NoThanksGame(object):
    def __init__(self,
                 playerInitialTokens: int = 11,
                 deckRange: range = range(3, 36),
                 totalDiscards: int = 4):
        if totalDiscards < 0:
            raise ValueError("The value of totalDiscards must be >= 0")
        if len(deckRange) <= totalDiscards:
            raise ValueError("The value of totalDiscards must be < total number of cards in the deck")
        if playerInitialTokens <= 0:
            raise ValueError("The value of playerInitialTokens must be > 0")
        self.players: List[BaseNoThanksPlayer] = []
        self.deck: List[int] = []
        self.discard: List[int] = []
        self.card: int = None
        self.tokens: int = 0
        self.deckRange = deckRange
        self.currentPlayerIndex: int = 0
        self.playerInitialTokens: int = playerInitialTokens
        self.totalDiscards: int = totalDiscards

    def AddPlayer(self, player) -> None:
        self.players.append(player)

    def NextPlayer(self) -> None:
        self.currentPlayerIndex += 1
        self.currentPlayerIndex %= len(self.players)

    def Pass(self, player) -> None:
        print("Player", self.currentPlayerIndex + 1, "Passes")
        player.tokens -= 1
        self.tokens += 1
        self.NextPlayer()

    def TakeCard(self, player) -> None:
        print("====> Player", self.currentPlayerIndex + 1, "Takes", self.card)
        player.tokens += self.tokens
        self.tokens = 0
        player.cards.append(self.card)
        self.Draw()

    def Draw(self) -> None:
        random.shuffle(self.deck)
        self.card = self.deck.pop()

    def PrintBoardInformation(self) -> None:
        print("Board Information")
        # Debug players should not see this information during game play
        # print("\tDiscard:", self.discard)
        # print("\tDeck:", self.deck)
        print("\tCards Remaining:", len(self.deck))
        print("\tCard:", self.card)
        print("\tTokens:", self.tokens)
        print("\tCurrent Player:", self.currentPlayerIndex + 1)

    def PrintPlayerInformation(self) -> None:
        print("Player Information")
        for playerIndex, player in enumerate(self.players):  # type: int, BaseNoThanksPlayer
            print("\tPlayer", playerIndex + 1)
            print("\t\tTokens:", player.tokens)
            print("\t\tCards:", sorted(player.cards))
            print("\t\tScore:", player.GetScore())

    def PrintScoreBoard(self) -> None:
        print("Score Board")
        for playerIndex, player in enumerate(self.players):  # type: int, BaseNoThanksPlayer
            print("\tPlayer", playerIndex + 1, player.GetScore(), "points")

    def SetupGame(self) -> None:
        self.DealTokens()
        self.InitializeDeck()
        self.Draw()

    def DealTokens(self) -> None:
        for player in self.players:  # type: BaseNoThanksPlayer
            player.tokens = self.playerInitialTokens

    def InitializeDeck(self) -> None:
        self.deck = list(self.deckRange)
        random.shuffle(self.deck)
        self.discard = self.deck[:self.totalDiscards]
        self.deck = self.deck[self.totalDiscards:]

    def GetCurrentPlayer(self) -> BaseNoThanksPlayer:
        return self.players[self.currentPlayerIndex]

    def PromptCurrentPlayer(self) -> None:
        currentPlayer: BaseNoThanksPlayer = self.GetCurrentPlayer()
        if currentPlayer.CanPass() and currentPlayer.WillPass(boardState=self):
            self.Pass(currentPlayer)
        else:
            self.TakeCard(currentPlayer)

    def RunGame(self) -> None:
        self.SetupGame()
        while self.deck:
            self.PrintBoardInformation()
            self.PrintPlayerInformation()
            self.PromptCurrentPlayer()
            print()
        self.PrintScoreBoard()
