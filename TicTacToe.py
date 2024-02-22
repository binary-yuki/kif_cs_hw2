"""
Author: Jeffery Raphael
Date: Feb 2024
Version: 4.0

Increase speed of learning by simplifying internal representation
of game state. Remove minimax & added ability to save policy.
"""

import random

RL_AGENT = 1
RANDOM_AGENT = 2
HUMAN_AGENT = 3
OTHER_AGENT = 7
TRAINING_MODE = 5
PLAYING_MODE = 6

# todo: replace this
RANDOM_NUMBER_SEED = random.random()
random.seed(RANDOM_NUMBER_SEED)


def createPlayer(letter, playerType=RANDOM_AGENT):
    """
    This function creates a player object

    param letter: A string; single character, e.g., 'X' or 'O'
    param playerType: Integer, RL_AGENT or HUMAN_AGENT
    """

    if playerType == RL_AGENT:
        return RLPlayer(letter)
    elif playerType == HUMAN_AGENT:
        return HUMANPlayer(letter)

    return Player(letter, playerType)


def train(player1, player2, episodes):
    """
    This function executes n (as specified by episodes) tictactoe games

    param player1: A Player object
    param player2: A Player object
    param episodes: Number of tictactoe games to play for training
    """

    for i in range(episodes):
        board = TicTacToe()
        board.setPlayers(player1, player2)
        runEpisode(board)


def runEpisode(board):
    """
    This function executes a single tictactoe game and updates
    the state value table after every move played by the RL agent.

    param board: A TicTacToe object
    """

    players = board.getPlayers()
    rlplayer = players[0]

    if not rlplayer.getType() == RL_AGENT:
        rlplayer = players[1]

    rlplayer.previousState = board.copy()
    while not board.isGameOver():
        player = board.next()
        player.makeMove(board)

    rlplayer.rewardState(board)


class TicTacToe:
    """
    This class represents the TicTacToe board. It draws the board and
    keeps track of the moves that have been made.
    """

    def __init__(self):
        """
        Creates a new empty board. Internally, the board is a 2D list.
        Empty squares are denotes with a single asterisk '*'
        """

        self.board = ['*', '*', '*', '*', '*', '*', '*', '*', '*']
        self.moveCount = 0
        self.lastMove = None
        self.remainingMoves = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        self.player1 = None
        self.player2 = None
        self.userQuit = False

    def setPlayers(self, player1, player2):
        """
        Initialises the players

        param player1: A Player object
        param player2: A Player object
        """

        self.player1 = player1
        self.player2 = player2

        self.player1.winner = False
        self.player2.winner = False

        self.player1.isTurn = True
        self.player2.isTurn = False

    def getPlayers(self):
        """
        Returns the players

        return: List of Player objects
        """
        return [self.player1, self.player2]

    def next(self):
        """
        Returns the player whose turn it is to move

        return: Player object
        """

        if self.player1.isTurn:
            self.player1.isTurn = False
            self.player2.isTurn = True
            return self.player1
        else:
            self.player1.isTurn = True
            self.player2.isTurn = False
            return self.player2

    def getWinner(self):
        """
        Returns the player that has won the gaem

        return: Player object or None
        """

        if self.isGameWon(self.player1.letter):
            return self.player1
        elif self.isGameWon(self.player2.letter):
            return self.player2
        elif self.isGameDraw() or self.userQuit:
            return None

    def isGameOver(self):
        """
        Determines if the game is over, True if it's over. Otherwise
        False

        return: True or False
        """

        if self.isGameWon('X'):
            return True

        if self.isGameWon('O'):
            return True

        if self.userQuit:
            return True

        if self.moveCount >= 9:
            return True

        return False

    def isGameDraw(self):
        """
        Determines if the game is a draw, True if it's a draw.
        Otherwise False

        return: True or False
        """

        if self.moveCount >= 9:
            return True

        return False

    def isGameWon(self, mark):
        """
        Checks to see if a player, specified by mark, has won the
        game; True if that player has one, otherwise False

        param mark: String, single character, e.g., 'X' or 'O'
        return: True or False
        """

        if self.isSameAs(mark, self.board[0], self.board[1], self.board[2]):
            return True

        if self.isSameAs(mark, self.board[3], self.board[4], self.board[5]):
            return True

        if self.isSameAs(mark, self.board[6], self.board[7], self.board[8]):
            return True

        if self.isSameAs(mark, self.board[0], self.board[3], self.board[6]):
            return True

        if self.isSameAs(mark, self.board[1], self.board[4], self.board[7]):
            return True

        if self.isSameAs(mark, self.board[2], self.board[5], self.board[8]):
            return True

        if self.isSameAs(mark, self.board[0], self.board[4], self.board[8]):
            return True

        if self.isSameAs(mark, self.board[2], self.board[4], self.board[6]):
            return True

        return False

    def isSameAs(self, char, a, b, c):
        """
        Checks if all four parameters are equal, if so, return True
        Otherwise False

        param char:  String, a character, e.g., 'X' or 'O'
        param a: String, a character, e.g., 'X' or 'O' or '*'
        param b: String, a character, e.g., 'X' or 'O' or '*'
        param c: String, a character, e.g., 'X' or 'O' or '*'
        return: True or False
        """

        if char == a and a == b and b == c:
            return True

        return False

    def drawBoard(self):
        """
        Displays the game on the screen/board.  It can only display the
        letters X and O.
        """

        letterX = ['  X     X  ', '   X   X   ', '    X X    ',
                   '     X     ', '    X X    ', '   X   X   ', '  X     X  ']
        letterO = ['   OOOOO   ', '  O     O  ', '  O     O  ',
                   '  O     O  ', '  O     O  ', '  O     O  ', '   OOOOO   ']

        tmp = []
        tmp.append((' ' * 11) + '@' + (' ' * 11) + '@' + (' ' * 11))
        lim = [[0, 3], [3, 6], [6, 9]]

        for i in range(3):
            # row = self.board[i]
            limits = lim[i]
            row = self.board[limits[0]:limits[1]]

            for j in range(7):
                msg = ""
                for k in range(3):
                    if row[k] == 'X':
                        msg += letterX[j]
                    elif row[k] == 'O':
                        msg += letterO[j]
                    else:
                        msg += ' ' * 11

                    if k != 2:
                        msg += '@'

                tmp.append(msg)

            if i != 2:
                tmp.append((' ' * 11)
                           + '@' + (' ' * 11)
                           + '@' + (' ' * 11))
                tmp.append('@' * 35)
                tmp.append((' ' * 11)
                           + '@' + (' ' * 11)
                           + '@' + (' ' * 11))

        tmp.append((' ' * 11) + '@' + (' ' * 11) + '@' + (' ' * 11))
        print("\n\n")
        for line in tmp:
            print(line)
        print("\n\n")

    def drawMiniBoard(self):
        """
        Displays the game on the screen/board.
        """

        print()
        print(self.board[0] + self.board[1] + self.board[2])
        print(self.board[3] + self.board[4] + self.board[5])
        print(self.board[6] + self.board[7] + self.board[8])
        print()

    def makeMove(self, location, mark):
        """
        Puts a letter (mark) on the board, at location, if it's
        legal to do so. Returns True if x, y is within bounds and the
        square has not been marked already; Otherwise False.

        param location: A list, [x,y] where x and y are coordinates on
                        tictactoe board (1 <= x <= 3 and 1 <= y <= 3)
        param mark: String, e.g., 'X' or 'O'
        return: True or False
        """

        if 0 <= location <= 8:

            if self.board[location] != '*':
                return False

            self.board[location] = mark
            self.moveCount += 1
            self.lastMove = location

            self.remainingMoves.remove(location)

            return True

        return False

    def copy(self):
        """
        Makes a copy of the tictactoe board.

        return: TicTacToe object
        """

        newBoard = TicTacToe()

        newBoard.board = self.board[:]
        newBoard.moveCount = self.moveCount
        newBoard.lastMove = self.lastMove
        newBoard.remainingMoves = self.remainingMoves[:]
        newBoard.player1 = self.player1
        newBoard.player2 = self.player2
        newBoard.userQuit = self.userQuit

        return newBoard

    def getKey(self, letter):
        """
        This method transform the 2D list which represents the board
        into a single string to be used as a key. In the key, the Xs
        and Os are replaced with L and T where L represents the letter
        (X or O) used by the learning agent and the T is the opponent.
        This allows the agent to learn by playing as X or O.

        param letter: String, the letter used by the learning agent.
        return: String, 9 characters long, of Ls, Ts and *s.
        """

        r = "".join(self.board)

        r = r.replace(letter, 'L')
        if letter == 'X':
            r = r.replace('O', 'T')
        else:
            r = r.replace('X', 'T')

        return r


class Player:
    """
    This class represents a person or agent playing tictactoe. The
    Player class also allows human's to play.
    """

    def __init__(self, letter, playerType=RANDOM_AGENT):
        """
        Creates a new player. When creating a Player you have to specify
        a letter and player type.  The letter is either 'X' or 'O'
        (both capitilised).  The player type can be: RANDOM_AGENT,
        RL_AGENT or HUMAN_AGENT.

        param letter: String, single character, can only be 'X' or 'O'
        param playerType: Integer, The type of player RANDOM_AGENT,
                        RL_AGENT or HUMAN_AGENT
        """

        self.letter = letter
        self.opponent = 'O'

        if letter == 'O':
            self.opponent = 'X'

        self.playerType = playerType

        self.name = "Unknown"
        self.rating = 1200
        self.gamesW = 0
        self.gamesD = 0
        self.gamesL = 0

        self.firstPlayer = True
        self.isTurn = True
        self.winner = False

    def getType(self):
        """
        This method returns the type of player, RANDOM_AGENT,
        RL_AGENT or HUMAN_AGENT.

        return: Integer
        """

        return self.playerType

    def makeMove(self, board):
        """
        This method selects a random move. This method should be similar
        to getHumanMove(...)

        param board: TicTacToe object
        """

        moveLegal = False

        while not moveLegal:
            loc = random.randint(0, 8)
            moveLegal = board.makeMove(loc, self.letter)


class HUMANPlayer(Player):
    """
    This class represents a person playing tictactoe.
    """

    def __init__(self, letter):
        """
        Creates a new human player.

        param letter: String, can only be 'X' or 'O'
        """

        super().__init__(letter, HUMAN_AGENT)

    def requestMove(self):
        """
        This method asks the user to enter a move, a number from 0 to 8
        inclusive

        return: Integer
        """

        userInput = input("Player " + self.letter +
                          ", enter a move (e.g. 0...8) : ")
        userInput = userInput.strip()

        if userInput == "quit":
            return None

        return int(userInput)

    def makeMove(self, board):
        """
        This method makes the move (updates the board) for the human
        player

        param board: A TicTacToe object
        """

        moveLegal = False

        while not moveLegal:
            playerMove = self.requestMove()

            if playerMove is None:
                board.userQuit = True
                moveLegal = True
            else:
                moveLegal = board.makeMove(playerMove, self.letter)


class Tournament:
    """
    This class performs a tournament between two tictactoe players.
    By default the board is not drawn.  If a human is playing in the
    tournament, call enableHumanPlayer() to show the board.
    """

    def __init__(self):
        """
        Creates a new tournament.
        """

        self.board = None
        self.humanPlaying = False

    def getBoard(self):
        """
        Gets the last tictactoe board that was played.  If no games
        were played then this is None
        return: TicTacToe object or None
        """

        return self.board

    def enableHumanPlayer(self):
        """
        This method enables the board drawing, i.e., if called
        the board is drawn during the tournament.  This should only
        be used if one of the players is human.
        """

        self.humanPlaying = True

    def start(self, player1, player2, games=1):
        """
        This method performs the tournament; n games are played.

        param player1: Player object
        param player2: Player object
        param games: Integer
        """

        for _ in range(games):

            self.game(player1, player2)
            self.elo(player1, player2)

            if self.humanPlaying:
                if player1.winner:
                    print(f'Winner: {player1.name}')
                elif player2.winner:
                    print(f'Winner: {player2.name}')
                else:
                    print(f'Draw')

    def game(self, p1, p2):
        """
        This method executes a single game of tictactoe between
        player1 and player2

        param p1: Player object
        param p2: Player object
        """

        self.board = TicTacToe()
        self.board.setPlayers(p1, p2)

        if self.humanPlaying:
            self.board.drawBoard()

        while not self.board.isGameOver():

            player = self.board.next()
            player.makeMove(self.board)

            if self.humanPlaying:
                self.board.drawBoard()

        player = self.board.getWinner()

        if player:
            player.winner = True

    def elo(self, player1, player2):
        """
        This method updates each player's rating according to the
        ELO rating system

        param player1: Player object
        param player2: Player object
        """

        K = 30
        qa = 10 ** (player1.rating / 400)
        qb = 10 ** (player2.rating / 400)

        e1 = qa / (qa + qb)
        e2 = qb / (qa + qb)

        if player1.winner:
            r1 = player1.rating + K * (1 - e1)
            r2 = player2.rating + K * (0 - e2)
            player1.gamesW += 1
            player2.gamesL += 1
        elif player2.winner:
            r1 = player1.rating + K * (0 - e1)
            r2 = player2.rating + K * (1 - e2)
            player2.gamesW += 1
            player1.gamesL += 1
        else:
            r1 = player1.rating + K * (1 - e1)
            r2 = player2.rating + K * (1 - e2)
            player1.gamesD += 1
            player2.gamesD += 1

        player1.rating = r1
        player2.rating = r2

    def printStats(self, players):
        """
        This method prints the stats (number of games won, lost, drawn
        and rating) for each player

        param players: List of Player objects
        """

        print()
        print(f'{"Agents":<7} {"Won":<4} {"Lost":<5} {"Draws":<6} {"Rating"}')
        print('-' * 32)

        for player in players:
            wins = player.gamesW
            lost = player.gamesL
            draws = player.gamesD
            rating = player.rating
            print(f'{player.name:<7} {wins:<4} {lost:<5} {draws:<6} {rating:4.1f}')

        print('\n\n')


class RLPlayer(Player):
    """
    This class represents a reinforcement learning agent.
    """

    def __init__(self, letter):
        """
        Creates a new RL player.

        param letter: String, can only be 'X' or 'O'
        """

        super().__init__(letter, RL_AGENT)

        self.learningRate = 0.0
        self.discountRate = 0.0
        self.epsilon = 0.0
        self.valueFunction = {}
        self.previousState = None
        self.mode = PLAYING_MODE

    def initTraining(self, learning, discount, epsilon):
        """
        Initialises RL hyper-parameters

        param learning: Float (0..1)
        param discount: Float (0..1)
        param epsilon: Float (0..1)
        """

        self.learningRate = learning
        self.discountRate = discount
        self.epsilon = epsilon
        self.previousState = None
        self.mode = TRAINING_MODE

    def setMode(self, mode):
        """
        Sets playing mode, TRAINING_MODE or PLAYING_MODE

        param mode: Integer
        """

        self.mode = mode

    def getMode(self):
        """
        Get's the playing mode

        return: Integer
        """

        return self.mode

    def getRLMove(self, board):
        """
        This method performs moves for the RL; it uses the learned
        policy.  It selects the best move according to the state
        value table.

        param board: TicTacToe object
        param epsilon: This variable controls how often the RL agent
                                exploits it's state value table rather then explore
                                new moves
        """

        bestMove = None
        bestValue = -99999

        for location in board.remainingMoves:
            cboard = board.copy()
            cboard.makeMove(location, self.letter)
            key = cboard.getKey(self.letter)

            if key in self.valueFunction:
                if self.valueFunction[key] >= bestValue:
                    bestValue = self.valueFunction[key]
                    bestMove = location

        if bestMove is not None:
            move = bestMove
        else:
            move = random.choice(board.remainingMoves)

        moveLegal = board.makeMove(move, self.letter)

        if not moveLegal:
            print('*** WARNING ILLEGAL MOVE BY RL ***')

    def valueOfState(self, key):
        """
        Gets the value of a game state.  If that state hasn't been
        encountered before then set it's value to 0

        param key: String
        return: Float
        """

        if key in self.valueFunction:
            return self.valueFunction[key]
        else:
            self.valueFunction[key] = 0
            return 0

    def save(self):
        """
        This method saves the learned policy.
        """

        with open('cse_policy_hw2.txt', 'w') as out:
            for k, v in self.valueFunction.items():
                out.write(k + ':' + str(v) + '\n')

    def _load(self):
        """
        This method loads a policy from a text file
        """

        with open('cse_policy_hw2.txt', 'r') as policy:
            for line in policy:
                kv = line.split(':')
                self.valueFunction[kv[0]] = float(kv[1])

    def makeMove(self, board):
        """
        This method makes a move for the RL player based on it's mode.

        param board: TicTacToe object
        """
        # todo: define Training mode and get a move for RL agent
        # Homework 2: Implement this method as described in the
        # assignment brief.  Write your code here.
        if self.mode == TRAINING_MODE:
            # if mode is training, make a random or best move based on epsilon
            # 如果是训练模式 根据 epsilon 做一个随机移动（取值0-1）或者最好的移动
            if random.random() < self.epsilon:
                # move randomly
                move = random.choice(board.remainingMoves)
                board.makeMove(move, self.letter)
            else:
                # call getRLMove to make the best move
                # 用 getRLMove 函数来做最好的移动
                self.getRLMove(board)
        else:
            # If mode is not training, always make the best move
            # 如果不是训练模式 做最好的移动
            self.getRLMove(board)

    def rewardState(self, board, prevBoard=None):
        """
        This method updates the value function 'table'; it rewards
        a game state

        param board: TicTacToe object
        param prevBoard: TicTacToe object or None
        """

        # Homework 2: Implement this method as described in the
        # assignment brief.  Write your code here.
        # if no previous board state, set it to current board
        if not prevBoard:
            prevBoard = self.previousState

        # Get keys from previous board and current board states
        prevBoardKey = prevBoard.getKey(self.letter)
        boardKey = board.getKey(self.letter)

        prevVal = self.valueOfState(prevBoardKey)

        # Calculate reward using the Bellman equation
        reward = self.getReward(board)
        value = prevVal + self.learningRate * (reward + self.discountRate * self.valueOfState(boardKey) - prevVal)

        # Update value function table
        self.valueFunction[prevBoardKey] = value

        # Update previous board state
        self.previousState = board.copy()

    def getReward(self, board):
        """
        This method analyses the board and determines a reward.  The
        exact reward scheme will be designed by the student.  This will
        be determined by the student.  However, it should return an
        integer value (negative or positive)

        param board: TicTacToe object
        return: Integer
        """

        # Homework 2: Implement this method as described in the
        # assignment brief.  Write your code here.  Your are free
        # to implement new methods as long as they do not over write
        # existing essential methods.

        # Make sure to replace this return state with your own code
        if board.isGameWon(self.letter):
            # if the RL player has won the game, return a positive reward
            return 10
        elif board.isGameWon(self.opponent):
            # if the opponent has won the game, return a negative reward
            return -10
        elif board.isGameDraw():
            # if the game is a draw, return a smaller positive reward
            return 5
        else:
            # for other states, return a neutral reward
            return 0
