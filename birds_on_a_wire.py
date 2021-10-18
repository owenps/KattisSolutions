l,d,n = list(map(int,input().split()))
birds = []
for _ in range(n):
   birds.append(int(input()))

if l <= 12:
   print(0)
else:
   extra_birds = 0
   if n == 0:
      extra_birds += ((l-12) // d)+1
   else:
      birds.sort()
      left = birds[0] - 6
      right = (l-6) - birds[-1]
      extra_birds += (left//d) + (right//d)
      for i in range(n-1):
         dist = birds[i+1] - birds[i]
         extra_birds += (dist//d)-1
   print(extra_birds)