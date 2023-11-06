from cards import Hand, Deck
from players import Dealer, UserPlayer


class GameRound:
    def __init__(self, player, dealer, deck):
        self._player = player
        self._dealer = dealer
        self._deck = deck

    def getBetUser(self):
        amount = int(input('Enter a bet amount: '))
        return amount

    def dealInitialCards(self):
        for i in range(2):
            self._player.addCard(self._deck.draw())
            self._dealer.addCard(self._deck.draw())
        print('Player hand: ')
        self._player.getHand().print()
        dealerCard = self._dealer.getHand().getCards()[0]
        print("Dealer's first card: ")
        dealerCard.print()

    def cleanupRound(self):
        self._player.clearHand()
        self._dealer.clearHand()
        print('Player balance: ', self._player.getBalance())

    def play(self):
        self._deck.shuffle()

        if self._player.getBalance() <= 0:
            print('Player has no more money =)')
            return
        userBet = self.getBetUser()
        self._player.placeBet(userBet)

        self.dealInitialCards()

        # User makes moves
        while self._player.makeMove():
            drawnCard = self._deck.draw()
            print('Player draws', drawnCard.getSuit(), drawnCard.getValue())
            self._player.addCard(drawnCard)
            print('Player score: ', self._player.getHand().getScore())

        if self._player.getHand().getScore() > 21:
            print('Player busts!')
            self.cleanupRound()
            return
        
        # Dealer makes moves
        while self._dealer.makeMove():
            self._dealer.addCard(self._deck.draw())
        
        # Determine winner
        if self._dealer.getHand().getScore() > 21:
            print('Player wins')
            self._player.receiveWinnings(userBet * 2)
        elif self._dealer.getHand().getScore() > self._player.getHand().getScore():
            print('Player loses')
        else:
            print('Game ends in a draw')
            self._player.receiveWinnings(userBet)
        self.cleanupRound()


player = UserPlayer(1000, Hand())
dealer = Dealer(Hand())

while player.getBalance() > 0:
    gameRound = GameRound(player, dealer, Deck()).play()