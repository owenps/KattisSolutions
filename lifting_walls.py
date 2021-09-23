def findcranes(locations,i=0,solution=[False,False,False,False]):
    if not locations:
        return 5
    new_solution = list(map(lambda x: x[0] | x[1], zip(locations[i],solution)))
    if i == len(locations)-1: # last element
        return 1 if all(new_solution) else 5
    else:
        no_use = 0 + findcranes(locations,i+1,solution)
        use = 1 + findcranes(locations,i+1,new_solution)
        return min(no_use,use)

length,width,n_locations,radius = list(map(int,input().split()))

walls = [(-length/2.0,0),(length/2.0,0),(0,-width/2.0),(0,width/2.0)]

radius = radius**2
eucdist2 = lambda x1,x2: (x1[1]-x2[1])**2+(x1[0]-x2[0])**2

locations = [] # [False,False,False,False]
for _ in range(n_locations):
    crane = tuple(map(int,input().split()))
    can_reach = []
    for wall in walls:
        can_reach.append(eucdist2(wall,crane) <= radius)
    if (can_reach not in locations) and any(can_reach):
        locations.append(can_reach) 

total = findcranes(sorted(locations,key=lambda x: sum(x))) # arrange crane locations by most reachable walls
print("Impossible") if total > 4 else print(total)