class disjoint_set():
    def __init__(self):
        self.parents = {}
        self.sizes = {}

    def find(self,x):
        temp = x
        visited = set()
        while (x != self.parents[x]):
            visited.add(x)
            x = self.parents[x]
        
        # truncate tree
        for node in visited:
            self.parents[node] = x

        return x
    
    def union(self,x,y):
        x_par = self.find(x) 
        y_par = self.find(y)
        
        if x_par != y_par: # not in same set
            # set x's parent to be y's parent
            self.parents[x_par] = y_par
            # increase y's size by x's size
            self.sizes[y_par] += self.sizes[x_par]
            return self.sizes[y_par]
        return self.sizes[x_par]

N = int(input())

for n in range(N):
    F = int(input())
    dset = disjoint_set()
    for f in range(F):
        a,b = input().split()
        if a not in dset.parents:
            dset.parents[a] = a
            dset.sizes[a] = 1
        if b not in dset.parents:
            dset.parents[b] = b
            dset.sizes[b] = 1
        print(dset.union(a,b))