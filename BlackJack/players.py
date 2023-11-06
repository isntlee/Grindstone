from abc import ABC, abstractmethod
from cards import Hand


class Player(ABC):
    def __init__(self, hand):
        self._hand = hand

    def getHand(self):
        return self._hand

    def clearHand(self):
        self._hand = Hand()

    def addCard(self, card):
        self._hand.addCard(card)

    @abstractmethod
    def makeMove(self):
        pass


class UserPlayer(Player):
    def __init__(self, balance, hand):
        super().__init__(hand)
        self._balance = balance

    def getBalance(self):
        return self._balance

    def placeBet(self, amount):
        if amount > self._balance:
            raise ValueError('Insufficient funds')
        self._balance -= amount
        return amount

    def receiveWinnings(self, amount):
        self._balance += amount

    def makeMove(self):
        if self.getHand().getScore() > 21:
            return False
        move = input('Draw card? [y/n] ')
        return move == 'y'
    

class Dealer(Player):
    def __init__(self, hand):
        super().__init__(hand)
        self._targetScore = 17

    def updateTargetScore(self, score):
        self._targetScore = score

    def makeMove(self):
        return self.getHand().getScore() < self._targetScore