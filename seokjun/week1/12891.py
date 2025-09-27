s, p = map(int, input().split(' '))
dna = input()
acgt = [int(x) for x in input().split(' ')]

password = {'A':acgt[0],'C':acgt[1],'G':acgt[2],'T':acgt[3]}

start = 0
cnt = {'A':0,'C':0,'G':0,'T':0}
#처음 p길이의 acgt개수 계산
for i in range(p):
    cnt[dna[i]] += 1

answer = 0

# 왼쪽으로 1칸씩 이동하면서 acgt개수 계산
while start <= s-p:
    valid = True
    for key in password.keys():
        if cnt[key] < password[key]:
            valid = False
            break

    if valid:
        answer += 1

    if start >= s-p:
        break

    cnt[dna[start]] -= 1
    cnt[dna[start+p]] += 1
    start += 1

print(answer)

