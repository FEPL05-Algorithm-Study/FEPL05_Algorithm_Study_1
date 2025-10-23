from collections import Counter

n, m = map(int, input().split())
dnas = [input() for _ in range(n)]

# dna1과 dna2의 Hamming_Distance를 구하는 함수
def Hamming_Distance(dna1,dna2):
    result = 0
    for i in range(m):
        if dna1[i]!=dna2[i]:
            result += 1
    return result

# Hamming_Distance의 총 합을 계산
def sum_Hamming_Distance(x):
    result = 0
    for dna in dnas:
        result += Hamming_Distance(x,dna)
    return result


d = [[] for _ in range(m)]

# d[i] = 각 dna에서 i번째 인덱스에 해당하는 문자를 저장
for dna in dnas:
    for i in range(m):
        d[i].append(dna[i])

s = ''

for i in range(m):
    # i번째 해당하는 문자들을 저장한 배열을 Counter로 개수를 세어줌
    c = list(Counter(d[i]).items())
    # 개수가 많은순, 사전순으로 빠른순으로 정렬
    c.sort(key=lambda x: (-x[1],x[0]))
    # 구할려는 dna s에 추가
    s += c[0][0]

print(s)
print(sum_Hamming_Distance(s))