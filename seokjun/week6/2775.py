from itertools import*

t=int(input())
for _ in range(t):
    k,n=int(input()),int(input())
    # 0층
    f=list(range(n+1))
    for _ in range(k):
        # 다음층은 이전층의 누적합 배열
        f=list(accumulate(f))
    print(f[n])