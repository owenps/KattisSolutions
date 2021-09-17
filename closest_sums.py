def findNearest(lst, target):
   distance = 1e10 # infinity
   closest_sum = None
   N = len(lst)
   for i in range(N-1):
      for j in range(i+1,N):
         s = lst[i] + lst[j]
         if abs(target - s) < distance: 
            distance = abs(target - s)
            closest_sum = s
   return closest_sum


counter = 0
while True:
   try: 
      counter += 1
      ans = []
      # Read Inputs
      nums = []
      for i in range(int(input())): # range(n)
         nums.append(int(input()))

      queries = []
      for i in range(int(input())): # range(m)
         q = int(input())
         queries.append(q)

         ans.append(findNearest(nums,q))
      
      print("Case {}:".format(counter))
      for a,q in zip(ans,queries):
         print("Closest sum to {} is {}.".format(q,a))


   except EOFError:
      break