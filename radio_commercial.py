


N, P = map(int,input().split())
commercials = list(map(lambda x: int(x)-P, input().split()))
dp = [0 for _ in range(len(commercials))]

if (all(c < 0 for c in commercials)): # if all negative take max
   print(max(commercials))

elif (all(c > 0 for c in commercials)): # if all profit take the whole array
   print(sum(commercials))

   