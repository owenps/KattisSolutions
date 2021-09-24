def countstars(sky,i_src,j_src):
    toExplore = [(i_src,j_src)]
    while len(toExplore) > 0:
        i,j = toExplore.pop()
        sky[i][j] = "X" # mark as explored
        # explore around it
        if i-1 >= 0 and sky[i-1][j] == "-":
            toExplore.append((i-1,j))
        if i+1 < len(sky) and sky[i+1][j] == "-":
            toExplore.append((i+1,j))
        if j-1 >= 0 and sky[i][j-1] == "-":
            toExplore.append((i,j-1))
        if j+1 < len(sky[0]) and sky[i][j+1] == "-":
            toExplore.append((i,j+1))
            
testnum = 0
while True:
    try: 
        testnum += 1
        m,n = input().split()
        m,n = int(m), int(n)
        sky = []
        count = 0
        for _ in range(m):
            sky.append(list(input()))
        
        for i in range(m):
            for j in range(n):
                if sky[i][j] == "-":
                    countstars(sky,i,j)
                    count += 1
        print("Case "+str(testnum)+": "+str(count))
    except EOFError:
        break