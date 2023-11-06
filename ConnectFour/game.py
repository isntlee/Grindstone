from player import Player
from grid import GridPosition, Grid, Style


class Style:
    RED = '\033[31m'
    YELLOW = '\033[33m'
    WHITE = '\033[37m'

    blank = '0 ' + WHITE
    Y =  YELLOW + 'Y ' + WHITE
    R =  RED + 'R ' + WHITE


class Game:
    def __init__(self, grid, connectN, targetScore):
        self._grid = grid
        self._connectN = connectN
        self._targetScore = targetScore

        self._players = [
            Player('Player 1', GridPosition.YELLOW),
            Player('Player 2', GridPosition.RED)
        ]

        self._score = {}
        for player in self._players:
            self._score[player.getName()] = 0

    def printBoard(self):
        print('Board:\n')
        grid = self._grid.getGrid()

        for i in range(len(grid)):
            row = ''
            for piece in grid[i]:
                if piece == GridPosition.EMPTY:
                    row += Style.blank
                elif piece == GridPosition.YELLOW:
                    row += Style.Y
                elif piece == GridPosition.RED:
                    row += Style.R
            print(row)
        print('')

    def playMove(self, player):
        self.printBoard()
        print(f"{player.getName()}'s turn")
        colCnt = self._grid.getColumnCount()
        moveColumn = int(input(f"Enter column between {0} and {colCnt - 1} to add piece: "))
        moveRow = self._grid.placePiece(moveColumn, player.getPieceColor())
        return (moveRow, moveColumn)

    def playRound(self):
        while True:
            for player in self._players:
                row, col = self.playMove(player)
                pieceColor = player.getPieceColor()
                if self._grid.checkWin(self._connectN, row, col, pieceColor):
                    self._score[player.getName()] += 1
                    return player

    def play(self):
        maxScore = 0
        winner = None
        while maxScore < self._targetScore:
            winner = self.playRound()
            print(f"{winner.getName()} won the round")
            maxScore = max(self._score[winner.getName()], maxScore)

            self._grid.initGrid() # reset grid
        print(f"{winner.getName()} won the game")


grid = Grid(6, 7)
game = Game(grid, 4, 2)
game.play()
