import time
from cards import Hand, Deck
from players import Dealer, UserPlayer


class GameRound:
    def __init__(self, player, dealer, deck):
        self._player = player
        self._dealer = dealer
        self._deck = deck

    def getBetUser(self):
        amount = int(input('\nEnter a bet amount: '))
        time.sleep(1)
        return amount

    def dealInitialCards(self):
        for i in range(2):
            self._player.addCard(self._deck.draw())
            self._dealer.addCard(self._deck.draw())
        self.gamePrint('\nPlayer hand: ', 2)
        self._player.getHand().print()
        dealerCard = self._dealer.getHand().getCards()[0]
        self.gamePrint("\nDealer's first card: ", 2)
        dealerCard.print()

    def cleanupRound(self):
        self._player.clearHand()
        self._dealer.clearHand()
        print('Player balance: ', self._player.getBalance())

    def gamePrint(self, string, delay):
        print(string)
        time.sleep(delay)

    def play(self):
        self._deck.shuffle()

        if self._player.getBalance() <= 0:
            self.gamePrint('Player has no more money =)', 2)
            return
        userBet = self.getBetUser()
        self._player.placeBet(userBet)

        self.dealInitialCards()

        # User makes moves
        while self._player.makeMove():
            drawnCard = self._deck.draw()
            print('\nPlayer draws', drawnCard.getSuit(), drawnCard.getValue())
            self._player.addCard(drawnCard)
            print('Player score: ', self._player.getHand().getScore())

        if self._player.getHand().getScore() > 21:
            self.gamePrint('\nPlayer busts!', 2)
            self.cleanupRound()
            return
        
        # Dealer makes moves
        while self._dealer.makeMove():
            self._dealer.addCard(self._deck.draw())
            time.sleep(2)
        
        # Determine winner
        if self._dealer.getHand().getScore() > 21:
            self.gamePrint('\nPlayer wins', 2)
            self._player.receiveWinnings(userBet * 2)
        elif self._dealer.getHand().getScore() > self._player.getHand().getScore():
            self.gamePrint('\nPlayer loses', 2)
        else:
            self.gamePrint('\nGame ends in a draw', 2)
            self._player.receiveWinnings(userBet)
        self.cleanupRound()


player = UserPlayer(1000, Hand())
dealer = Dealer(Hand())

while player.getBalance() > 0:
    gameRound = GameRound(player, dealer, Deck()).play()