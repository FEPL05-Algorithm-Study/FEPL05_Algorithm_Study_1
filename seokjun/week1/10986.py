n, m = map(int, input().split(' '))
a = arr = list(map(int, input().split(' ')))[int(x) for x in input().split(' ')]

r = [0]*n

s = 0
# i,j까지 합이 나누어떨어지기 위해서 mod(S[j]-S[i-1])=0 
# mod(S[i-1])=mod(S[j])를 계산하기 위한 나머지배열 생성
for i in range(n):
    s += a[i]
    r[i] = s%m


cnt = {}
# cnt 딕셔너리에 key:나머지 value:해당 나머지가 등장한 개수 저장
for i in range(n):
    if r[i] in cnt:
        cnt[r[i]] += 1
    else:
        cnt[r[i]] = 0

answer = 0
# cnt에서 같은 나머지가 n번 등장했다면, i, j 쌍의 가짓수 = nC2
# 만약 나머지가 0이라면 (n+1)C2
for key, value in cnt.items():
    if key==0:
        value = value + 1
    answer += value * (value+1) / 2

print(int(answer))

