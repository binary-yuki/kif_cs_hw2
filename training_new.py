import TicTacToe1 as ttt


def main():
    # Players
    rlAgent = ttt.createPlayer('X', ttt.RL_AGENT)
    rlAgent.name = 'RL Agent'

    partner = ttt.createPlayer('O', ttt.RANDOM_AGENT)
    partner.name = "Random"

    # Training Session 1
    rlAgent.initTraining(0.80465, 0.259703, 0.8265486)
    ttt.train(rlAgent, partner, 40000)
    rlAgent.save()

    # Training Session 2 Optional
    rlAgent.initTraining(0.8222, 0.46471809, 0.382242)  # learning rate, epsilon, gamma
    ttt.train(partner, rlAgent, 40000)

    # Evaluation
    rlAgent.setMode(ttt.PLAYING_MODE)
    tournament = ttt.Tournament()
    tournament.start(rlAgent, partner, 30)
    tournament.start(partner, rlAgent, 30)
    tournament.printStats([rlAgent, partner])
    print("learning rate: ", rlAgent.learningRate)


main()
