def doorman(diff, queue, max_diff):
   if abs(diff) > max_diff:
      return -1
   if not queue:
      return 0

   if len(queue) == 1 or queue[0] == queue[1]:
      new_diff = diff - 1 if queue[0] == "W" else diff + 1
      return 1 + doorman(new_diff, queue[1:], max_diff)
   else: # MW or WM
      return 2 + doorman(diff,queue[2:],max_diff)
   
X = int(input())
queue = input()

print(doorman(0,queue,X))