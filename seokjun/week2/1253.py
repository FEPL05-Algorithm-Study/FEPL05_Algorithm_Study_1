n = int(input())
arr = list(map(int,input().split(' ')))

arr.sort()

# good 여부를 판별하는 함수
def valid(i):
    # i번째수-j번째수를 저장하는 set
    s = set()  
    for j in range(n):
        if i == j:
            continue

        if arr[j] in s:
            return True
        s.add(arr[i]-arr[j])
    return False

answer = 0
for i in range(n):
    answer += int(valid(i))

print(answer)
