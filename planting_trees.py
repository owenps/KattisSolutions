N = int(input()) # Number of seedlings
T = list(map(int,input().split()))

T = sorted(T, reverse=True)

days = 0
last_tree = -1
for i,tree in enumerate(T):
   end_day = tree + i + 1
   last_tree = max(last_tree,end_day)
print(last_tree + 1)