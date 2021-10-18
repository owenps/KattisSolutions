def calcLandmark(m,chars,constraint=False):
   m_copy = [list(l) for l in m]
   num = 0
   for i,l in enumerate(m_copy):
      for j,pt in enumerate(l):
         if pt in chars:
            explore(m_copy,i,j,chars,constraint)
            num += 1
   return num

def explore(m,i_src,j_src,chars_src,constraint):
   toExplore = {(i_src,j_src)}
   chars = chars_src
   # look north, south, east and west
   while toExplore:
      i,j = toExplore.pop()
      
      if constraint and m[i][j] == "B":
         # If we are on a bridge buses can only travel to another bridge tile
         chars = ["B","X"]
      elif constraint and m[i][j] == "#":
         # If we are on a land tile we can only travel to land or end-of-bridge tile
         chars = ["X","#"]
      elif constraint:
         chars = chars_src

      m[i][j] = '.' # denote tile as explored
      # explore
      if i-1 >= 0 and m[i-1][j] in chars:
         toExplore.add((i-1,j))
      if i+1 < len(m) and m[i+1][j] in chars:
         toExplore.add((i+1,j))
      if j-1 >= 0 and m[i][j-1] in chars:
         toExplore.add((i,j-1))
      if j+1 < len(m[0]) and m[i][j+1] in chars:
         toExplore.add((i,j+1))



Maps = []
m = None
while True:
   try:
      l = input()
      if len(l) == 0: # empty line => new map
         Maps.append(m)
         m = []
         continue
      if m is None:
         m = []
      m.append(l) 
      
   except EOFError:
      Maps.append(m)
      break

for i,m in enumerate(Maps):
   print(f"Map {i+1}\nislands: {calcLandmark(m,['X','#'])}\nbridges: {calcLandmark(m,['B'])}\nbuses needed: {calcLandmark(m,['#','B','X'],True)}")
   if i != len(Maps) -1:
      print()
