a = input()
b = input()
c = input()

player = {'a': a, 'b': b, 'c': c}

fin = False
turn = 'a'
winner = ''
while not fin:
    if len(player[turn]) == 0:
        fin = True
        winner = turn
        break
    characterNextTurn = player[turn][0]

    player[turn] = player[turn][1:]
    turn = characterNextTurn

print(winner.upper())