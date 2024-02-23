import random

import TicTacToe1 as ttt

BEST_CONFIGS = []

rates = []
et_rates = []
dis_rates = []


def _append_rate():
    for i in range(3000):
        rate = random.randint(100000, 999999) / 1000000
        if rate not in rates:
            rates.append(rate)
    print(rates)
    return rates


def _append_et_rate():
    for i in range(3000):
        et_rate = random.randint(100000, 999999) / 1000000
        if et_rate not in et_rates:
            et_rates.append(et_rate)
    print(et_rates)
    return et_rates


def _append_dis_rate():
    for i in range(3000):
        dis_rate = random.randint(100000, 999999) / 1000000
        if dis_rate not in dis_rates:
            dis_rates.append(dis_rate)
    return dis_rates


def train_agent():
    # Players
    rlAgent = ttt.createPlayer('X', ttt.RL_AGENT)
    rlAgent.name = 'RL Agent'
    partner = ttt.createPlayer('O', ttt.RANDOM_AGENT)
    partner.name = "Random"
    _append_et_rate()
    _append_dis_rate()
    _append_rate()
    for rate in rates:
        for et_rate in et_rates:
            for dis_rate in dis_rates:
                # Training Session 1
                rlAgent.initTraining(rate, et_rate, dis_rate)
                ttt.train(rlAgent, partner, 1000)
                # Training Session 2 Optional
                rlAgent.initTraining(rate, et_rate, dis_rate)
                ttt.train(partner, rlAgent, 1000)
                # Evaluation
                rlAgent.setMode(ttt.PLAYING_MODE)
                tournament = ttt.Tournament()
                tournament.start(rlAgent, partner, 5)
                tournament.start(partner, rlAgent, 5)
                config = (rate, et_rate, dis_rate, rlAgent.rating)
                BEST_CONFIGS.append(config)
                print(
                    f"Configuration: Rate = {rate}, et_rate = {et_rate}, dis_rate = {dis_rate}, Rating = {rlAgent.rating}")
    # Sort configurations by rating in descending order
    # 排序配置按评级降序
    BEST_CONFIGS.sort(key=lambda x: x[3], reverse=True)


if __name__ == "__main__":
    train_agent()
