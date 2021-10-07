N, K = map(int,input().split())
left, right = 0, 1
gallery = []
for i in range(N):
    gallery.append(list(map(int,input().split())))
input() # 0 0
gallery.reverse() # for intuition, working bottom up

gallery_sum = 0
for l,r in gallery:
    gallery_sum += l + r

if K == 0:
    print(gallery_sum)
    quit()

# k is the number of rooms to close
# r is the index of top row included
# c is the left (1) or right (0) subgallery
dp = [[[1e6, 1e6] for _ in range(N)] for _ in range(K+1)]
for n in range(len(dp[0])):
    dp[0][n] = [0,0] # when k=0 we don't remove any rooms
dp[1][0][left] = gallery[0][left]
dp[1][0][right] = gallery[0][right]

for r in range(1,N):
    for k in range(1,K+1):
        dp[k][r][left] = min(
            dp[k-1][r-1][left] + gallery[r][left], # if we block the top left room
            # don't block top left room, so use best solution for r-1
            dp[k][r-1][left], 
            dp[k][r-1][right]
        )
        dp[k][r][right] = min(
            dp[k-1][r-1][right] + gallery[r][right], # if we block the top right room
            # don't block top right room, so use best solution for r-1
            dp[k][r-1][left], 
            dp[k][r-1][right]
        )

print(gallery_sum - min(dp[K][N-1][left], dp[K][N-1][right]))