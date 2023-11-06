from enum import Enum
import random

class Suit(Enum):
    CLUBS, DIAMONDS, HEARTS, SPADES = 'clubs', 'diamonds', 'hearts', 'spades'


class Card:
    def __init__(self, suit, value):
        self._suit = suit
        self._value = value
    
    def getSuit(self):
        return self._suit

    def getValue(self):
        return self._value

    def print(self):
        print(self.getSuit(), self.getValue())


class Hand:
    def __init__(self):
        self._score = 0
        self._cards = []

    def addCard(self, card):
        self._cards.append(card)
        if card.getValue() == 1:
            self._score += 11 if self._score + 11 <= 21 else 1
        else:
            self._score += card.getValue()
        print('Score: ', self._score)

    def getScore(self):
        return self._score

    def getCards(self):
        return self._cards

    def print(self):
        for card in self.getCards():
            print(card.getSuit(), card.getValue())


class Deck:
    def __init__(self):
        self._cards = []
        for suit in Suit:
            for value in range(1, 14):
                self._cards.append(Card(suit, min(value, 10)))

    def print(self):
        for card in self._cards:
            card.print()

    def draw(self):
        return self._cards.pop()

    def shuffle(self):
        for i in range(len(self._cards)):
            j = random.randint(0, 51)
            self._cards[i], self._cards[j] = self._cards[j], self._cards[i]