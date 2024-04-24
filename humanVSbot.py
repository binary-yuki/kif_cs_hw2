import TicTacToe as ttt


def main():
    # Players
    player1 = ttt.createPlayer('X', ttt.HUMAN_AGENT)
    player1.name = 'Alice'

    player2 = ttt.createPlayer('O', ttt.minAndMAx)
    player2.name = "Bob"

    # Create board
    board = ttt.TicTacToe()
    board.setPlayers(player2, player1)
    board.drawBoard()

    # Run Game
    while not board.isGameOver():
        player = board.next()
        player.makeMove(board)
        board.drawBoard()
    winner = board.getWinner()

    if winner:
        print(f'Congratulations {winner.name}')


main()
