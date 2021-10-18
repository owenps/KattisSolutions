N = int(input())
A = list(map(int,input().split()))
A_rev = list(reversed(A))
pivots = 0
max_arr, min_arr = [A[0]],[A[-1]]
# build max and min arrays
for i in range(1,N):
   max_arr.append(max(max_arr[i-1],A[i]))
   min_arr.append(min(min_arr[i-1],A_rev[i]))

min_arr = list(reversed(min_arr))
# find pivots
for i in range(N):
   if max_arr[i] <= A[i] and A[i] <= min_arr[i]:
      pivots += 1
print(pivots)