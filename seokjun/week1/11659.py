n, m = map(int, input().split(' '))
arr = [int(x) for x in input().split(' ')]
pair = [[int(x) for x in input().split(' ')] for _ in range(m)] 

s = 0
sumArr = [0]*(n+1)
# i부터j까지의 합은 S[j]-S[i+1]
for i in range(n):
    s += arr[i]
    sumArr[i+1] = s


for i, j in pair:
    print(sumArr[j]-sumArr[i-1])