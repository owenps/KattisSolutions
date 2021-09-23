def findmoves(game):
    res = []
    offset = -1
    while True:
        offset = game.find("-oo",offset+1)
        if offset == -1:
            break
        res.append((offset,"o--"))
    offset = -1
    while True:
        offset = game.find("oo-",offset+1)
        if offset == -1:
            break
        res.append((offset,"--o"))
    return res
    

def playgame(game):
    moves = findmoves(game)
    if len(moves) == 0:
        return game.count("o")
    
    # iterate all possible moves and return the smallest count
    counts = []
    for ind,nxt in moves:
        counts.append(playgame(game[:ind] + nxt + game[ind+3:]))

    return min(counts)

N = int(input())
games = []
for _ in range(N):
    games.append(input())

for game in games:
    print(playgame(game))