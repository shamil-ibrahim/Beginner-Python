from random import choice

players = []
file = open('players.txt', 'r')
players = file.read().splitlines()

teams = []
file = open('teams.txt', 'r')
teams = file.read().splitlines()

print('\nPlayers: ', players)
print('Teams: ', teams)

teamA = []
teamB = []

while len(players) > 0:
	playerA = choice(players)
	teamA.append(playerA)
	players.remove(playerA)

	if players == []:
		break

	playerB = choice(players)
	teamB.append(playerB)
	players.remove(playerB)

print('\nTeam A: ', teamA)
print('Team B: ', teamB)
