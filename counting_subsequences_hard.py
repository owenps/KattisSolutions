T = int(input())

for t in range(T):
    input()
    N = int(input())
    S = list(map(int,input().split()))
    occurences = {0:1} # sum_i : num. occurences of sum_i
    count = 0
    total = 0
    for i in range(N):
        total += S[i]
        if total - 47 in occurences:
            count += occurences[total - 47]
        
        occurences[total] = occurences[total]+1 if total in occurences else 1
    print(count)