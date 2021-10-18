a,b,c,n = list(map(int,input().split()))
if n < 3 or a+b+c < n or not all([a,b,c]):
   print("NO")
else:
   print("YES") 