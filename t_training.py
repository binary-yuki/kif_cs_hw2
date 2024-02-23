import TicTacToe1 as ttt


def main():
    # # Players
    # rlAgent = ttt.createPlayer('X', ttt.RL_AGENT)
    # rlAgent.name = 'RL Agent'
    #
    # partner = ttt.createPlayer('O', ttt.RANDOM_AGENT)
    # partner.name = "Random"
    # 创建一个'X'标记的binaryYukiBot的实例
    partner = ttt.binaryYukiBot('X')
    partner.name = "YukiBot"

    # 创建一个RLPlayer
    rlAgent = ttt.RLPlayer('O')
    rlAgent.name = "RL Agent"

    # Training Session 1
    rlAgent.initTraining(0.867224, 0.309477, 0.228002)
    ttt.train(rlAgent, partner, 1000)
    rlAgent.save()

    # Training Session 2 Optional
    rlAgent.initTraining(0.867224, 0.3, 0.2077)
    ttt.train(partner, rlAgent, 1000)

    # Evaluation
    rlAgent.setMode(ttt.PLAYING_MODE)
    tournament = ttt.Tournament()
    tournament.start(rlAgent, partner, 500)
    tournament.start(partner, rlAgent, 500)
    tournament.printStats([rlAgent, partner])


def epoch_2():
    # 创建一个RLPlayer
    import subprocess
    subprocess.run(["python3", "training.py"])


if __name__ == '__main__':
    from time import sleep
    from tqdm import tqdm
    # main的进度条
    for i in tqdm(range(100)):
        sleep(0.01)
    epoch_2()
    print("epoch_2训练完成")
    # epoch_2的进度条
    for i in tqdm(range(100)):
        sleep(0.01)
    main()
    print("训练完成")
    exit(1)
