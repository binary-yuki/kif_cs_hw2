import TicTacToe1 as ttt


def main():
    # Players
    rlAgent = ttt.createPlayer('X', ttt.RL_AGENT)
    rlAgent.name = 'RL Agent'

    partner = ttt.createPlayer('O', ttt.RANDOM_AGENT)
    partner.name = "Random"

    # Training Session 1
    rlAgent.initTraining(0.867224, 0.309477, 0.228002)
    ttt.train(rlAgent, partner, 1000)
    rlAgent.save()

    # Training Session 2 Optional
    rlAgent.initTraining(0.867224, 0.3, 0.2077)
    ttt.train(partner, rlAgent, 3000)

    # Evaluation
    rlAgent.setMode(ttt.PLAYING_MODE)
    tournament = ttt.Tournament()
    tournament.start(rlAgent, partner, 50)
    tournament.start(partner, rlAgent, 50)
    tournament.printStats([rlAgent, partner])


main()
