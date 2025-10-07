import sys

N = int(sys.stdin.readline())

sum_total = 0
max_num = 0 

for i in range(N) : 
   num_list = list(map(int, sys.stdin.readline().split()))
   run = max(num_list[0], num_list[1])
   trick = num_list[2:]
   first_try = max(trick)
   trick.remove(first_try)
   second_try = max(trick)

   sum_total = run + first_try + second_try
   if sum_total > max_num : 
      max_num = sum_total

print(max_num)