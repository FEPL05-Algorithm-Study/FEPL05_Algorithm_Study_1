import sys

input = sys.stdin.readline

T = int(input())

cent = [25, 10, 5, 1]

for i in range(T):
    change = []
    c = int(input())

    for j in cent:
        change.append(str(c // j))
        c %= j

    print(' '.join(change))

    
    
    

    
    
