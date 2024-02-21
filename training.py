import TicTacToe as ttt

def main():

	# Players
	rlAgent = ttt.createPlayer('X', ttt.RL_AGENT)
	rlAgent.name = 'RL Agent'

	partner = ttt.createPlayer('O', ttt.RANDOM_AGENT)
	partner.name = "Random"

	# Training Session 1
	rlAgent.initTraining(0.1, 0.2, 0.3)
	ttt.train(rlAgent, partner, 1000)
	rlAgent.save()

	# Training Session 2 Optional
	# rlAgent.initTraining(0.1, 0.2, 0.3)
	# ttt.train(partner, rlAgent, 1000)

	# Evaluation
	rlAgent.setMode(ttt.PLAYING_MODE)
	tournament = ttt.Tournament()
	tournament.start(rlAgent, partner, 5)
	tournament.start(partner, rlAgent, 5)
	tournament.printStats([rlAgent, partner])

main()
