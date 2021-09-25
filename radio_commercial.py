N, P = map(int,input().split())
C = list(map(lambda x: int(x)-P, input().split())) # commerical breaks

if (all(c < 0 for c in C)): # if all negative take max
   print(max(C))

elif (all(c > 0 for c in C)): # if all profit take the whole array
   print(sum(C))

# our recurrence then looks as follows
# S(i) = { C[i] if i=0, max{S(i-1) + C[i], C[i]} }
# where S(i) is the maximum profit over all subsequences ending at i. 
# where C is our list of commerical breaks
# The lhs is adding C[i] to the subsequence, the rhs is starting a new one
S = [C[0]] 
for i in range(1,len(C)):
   S.append(max(S[i-1]+C[i],C[i]))
print(max(S))
      
