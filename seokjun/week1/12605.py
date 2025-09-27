n = int(input())
arr = [input() for _ in range(n)]

for i in range(n):
    str = arr[i].split(' ')
    str.reverse()

    print(f"Case #{i+1}: {' '.join(str)}")