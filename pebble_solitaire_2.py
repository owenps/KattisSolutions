state_space = {}
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

def solve(game, state_space=state_space):
   if game in state_space:
      return state_space[game]
   moves = findmoves(game) # (index,new_board_part)
   if len(moves) == 0:
      state_space[game] = game.count("o")
      return state_space[game]
   
   vals = []
   for ind,nxt in moves:
      board = game[:ind] + nxt + game[ind+3:]
      if board in state_space:
         v = state_space[board]
      else:
         v = solve(board)
      vals.append(v)   

   state_space[game] = min(vals)
   return state_space[game]     

N = int(input())
games = []
for _ in range(N):
    games.append(input())

for game in games:
   print(solve(game))