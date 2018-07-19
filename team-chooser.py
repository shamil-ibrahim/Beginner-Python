from random import choice

players = ['Sam', 'John', 'Mark', 'Elon', 'Joy', 'Tim', 'Rony', 'Chan']
teams = ['Python', 'Java', 'Ruby', 'Javascript', 'Hadoop', 'Kotlin']

print('\nPlayers: ', players)
print('Teams: ', teams)

teamA = []
teamB = []

while len(players) > 0:
	playerA = choice(players)
	teamA.append(playerA)
	players.remove(playerA)

	if players = []:
		break;
	
	playerB = choice(players)
	teamB.append(playerB)
	players.remove(playerB)

print('\nTeam A: ', teamA)
print('Team B: ', teamB)
