import random
from typing import List

from nothankssim.BaseNoThanksPlayer import BaseNoThanksPlayer


class NoThanksGame(object):
    def __init__(self, startingTokens: int=11):
        self.players: List[BaseNoThanksPlayer] = []
        self.scores = {}
        self.deck: List[int] = []
        self.discard: List[int] = []
        self.card: int = None
        self.tokens: int = 0
        self._currentPlayerIndex: int = 0
        self.startingTokens: int = startingTokens
        self.lowestCard: int = 3
        self.highestCard: int = 35
        self.totalDiscards: int = 4
        self.eventLog: List = []

    def addPlayer(self, player):
        self.players.append(player)

    def run(self):
        self._dealTokens()
        self._initializeDeck()
        self._drawCard()
        while self.card:
            self._printBoardInformation()
            self._printPlayerInformation()
            self._promptCurrentPlayer()
        self._printBoardInformation()
        self._printPlayerInformation()
        self._printScoreBoard()

    def _nextPlayer(self):
        self._currentPlayerIndex += 1
        self._currentPlayerIndex %= len(self.players)

    def _logEvent(self, event):
        self.eventLog.append(event)

    def _passCard(self, player):
        # print("Player", player, "Passes On", self.card)
        player.passCard()
        self.tokens += 1
        self._logEvent(player.name + " passes on " + str(self.card))

    def _takeCard(self, player):
        # print("Player", player, "Takes", self.card)
        self._logEvent(player.name + " takes " + str(self.card) + " and " + str(self.tokens) + " tokens")
        player.takeCard(self.card, self.tokens)
        self.card = None
        self.tokens = 0

    def _drawCard(self):
        if self.deck:
            random.shuffle(self.deck)
            self.card = self.deck.pop()

    def _printBoardInformation(self):
        print("Board Information")
        # Debug players should not see this information during game play
        print("\tDiscard:", self.discard)
        print("\tDeck:", self.deck)
        print("\tCard:", self.card)
        print("\tTokens:", self.tokens)
        print("\tCurrent Player:", self._getCurrentPlayer().name)

    def _printPlayerInformation(self):
        print("Player Information")
        for player in self.players:
            print("\tPlayer", player.name)
            print("\t\tTokens:", player.tokens)
            print("\t\tCards:", sorted(player.cards))
            print("\t\tScore:", player.getCurrentScore())

    def _printScoreBoard(self):
        print("Score Board")
        for player in self.players:
            print("\tPlayer", player.name, player.getCurrentScore(), "points")

    def _dealTokens(self):
        for player in self.players:
            player.tokens = self.startingTokens

    def _resetPlayers(self):
        for player in self.players:  # type: BaseNoThanksPlayer
            player.reset()

    def _initializeDeck(self):
        self.deck = list(range(self.lowestCard, self.highestCard + 1))
        random.shuffle(self.deck)
        self.discard = self.deck[:self.totalDiscards]
        self.deck = self.deck[self.totalDiscards:]

    def _getCurrentPlayer(self):
        return self.players[self._currentPlayerIndex]

    def _promptCurrentPlayer(self):
        currentPlayer: BaseNoThanksPlayer = self._getCurrentPlayer()
        if currentPlayer.hasTokens() and currentPlayer.willPass():
            self._passCard(currentPlayer)
            self._nextPlayer()
        else:
            self._takeCard(currentPlayer)
            self._drawCard()
