while True:
   N,M = list(map(int,input().split()))

   if not (N and M): # N,M = 0
      break
   call_itervals = []
   for n in range(N):
      _,_,strt,dur = list(map(int,input().split()))
      call_itervals.append((strt,strt+dur))
   for m in range(M):
      strt, dur = list(map(int,input().split()))
      end = strt + dur
      total = 0
      for call_start,call_end in call_itervals:
         total += 1 if any((call_start <= strt < call_end, 
                           strt <= call_start < end, 
                           call_start < strt and call_end > end )) else 0
      print(total)
