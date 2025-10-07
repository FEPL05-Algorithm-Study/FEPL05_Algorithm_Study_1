import sys

number = int(sys.stdin.readline())
n = [0] * 100000

for _ in range(number) : 
    n[int(sys.stdin.readline())] += 1

for i in range(len(n)) : 
    if n[i] != 0 :
        for _ in range(n[i]) : 
            print(i)