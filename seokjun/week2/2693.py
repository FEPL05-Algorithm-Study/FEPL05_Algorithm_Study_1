t = int(input())
cases = [list(map(int,input().split(' '))) for _ in range(t)]

for arr in cases:
    arr.sort(reverse=True)
    print(arr[2])