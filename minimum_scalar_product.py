T = int(input())

for t in range(T):
   n = int(input())
   X = sorted(list(map(int,input().split())))
   Y = sorted(list(map(int,input().split())), reverse=True)

   sp = 0
   for x,y in zip(X,Y):
      sp += x*y
   print("Case #{}: {}".format(t+1,sp))