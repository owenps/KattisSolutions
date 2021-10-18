s,c,k = list(map(int,input().split()))
socks = sorted(list(map(int,input().split())))

if socks[-1]-socks[0] < k and c >= s:
   print(1)
else:
   # The idea here is to stuff as many socks as we can into one machine
   num_machines = 0
   available = c
   used_sock = None
   while socks:
      sock = socks[0]
      if available == c: # machine is empty
         num_machines += 1
         used_sock = socks.pop(0)
         available -= 1

      elif available == 0 or abs(used_sock-sock) > k:
         machine = []
         available = c

      elif k >= abs(used_sock-sock): # sock is within colour diff
         socks.pop(0)
         available -= 1
      
   print(num_machines)