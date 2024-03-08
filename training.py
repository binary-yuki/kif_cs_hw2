import TicTacToe as ttt


# seed 3937276738987654567898734572
def main():
    # Players
    rlAgent = ttt.createPlayer('X', ttt.RL_AGENT)
    rlAgent.name = 'RL Agent'

    partner = ttt.createPlayer('O', ttt.RANDOM_AGENT)
    partner.name = "Random"

    win_seeker = ttt.createPlayer('O', ttt.minAndMAx)
    partner.name = "MinMax"

    always_win = ttt.createPlayer('O', ttt.WinSeekingBot)
    partner.name = "WinSeeker"

    strategyBot = ttt.createPlayer('O', ttt.StrategicAgent)
    partner.name = "StrategyBot"

    crossBot = ttt.createPlayer('O', ttt.DiagonalWinBot)
    partner.name = "DiagonalWinBot"

    killerBot = ttt.createPlayer('O', ttt.ForkPreventionBot)
    partner.name = "ForkPreventionBot"

    # Training Session 1
    rlAgent.initTraining(0.79, 0.731, 0.801)
    ttt.train(rlAgent, partner, 90000)
    rlAgent.save()

    # Training Session 2 Optional
    rlAgent.initTraining(0.7611, 0.68, 0.72)
    ttt.train(partner, rlAgent, 40000)
    rlAgent.save()

    # Training Session 3 Optional
    rlAgent.initTraining(0.7911, 0.77, 0.781)
    ttt.train(win_seeker, rlAgent, 40000)
    rlAgent.save()

    # Training Session 4 Optional
    rlAgent.initTraining(0.7711, 0.93, 0.701)
    ttt.train(always_win, rlAgent, 40000)
    rlAgent.save()

    # Training Session 5 Optional
    rlAgent.initTraining(0.7711, 0.66, 0.701)
    ttt.train(rlAgent, win_seeker, 40000)
    rlAgent.save()

    # Training Session 6 Optional
    rlAgent.initTraining(0.7711, 0.39, 0.701)
    ttt.train(rlAgent, always_win, 40000)
    rlAgent.save()

    # Training Session 7 Optional
    rlAgent.initTraining(0.8111, 0.79, 0.771)
    ttt.train(strategyBot, rlAgent, 40000)
    rlAgent.save()

    # Training Session 8 Optional
    rlAgent.initTraining(0.7111, 0.669, 0.671)
    ttt.train(rlAgent, strategyBot, 40000)
    rlAgent.save()

    rlAgent.initTraining(0.7911, 0.77, 0.781)
    ttt.train(win_seeker, rlAgent, 40000)
    rlAgent.save()

    # Training Session 4 Optional
    rlAgent.initTraining(0.7711, 0.93, 0.701)
    ttt.train(always_win, rlAgent, 40000)
    rlAgent.save()

    rlAgent.initTraining(0.7911, 0.77, 0.781)
    ttt.train(crossBot, rlAgent, 40000)
    rlAgent.save()

    rlAgent.initTraining(0.7711, 0.93, 0.701)
    ttt.train(killerBot, rlAgent, 40000)
    rlAgent.save()

    rlAgent.initTraining(0.7911, 0.77, 0.781)
    ttt.train(rlAgent, killerBot, 40000)
    rlAgent.save()

    # Training Session 4 Optional
    rlAgent.initTraining(0.7711, 0.93, 0.701)
    ttt.train(rlAgent, crossBot, 40000)
    rlAgent.save()

    rlAgent.initTraining(0.79, 0.731, 0.801)
    ttt.train(rlAgent, partner, 90000)
    rlAgent.save()


    # Evaluation
    rlAgent.setMode(ttt.PLAYING_MODE)
    tournament = ttt.Tournament()
    tournament.start(rlAgent, partner, 30)
    tournament.start(partner, rlAgent, 30)
    tournament.printStats([rlAgent, partner])


main()
