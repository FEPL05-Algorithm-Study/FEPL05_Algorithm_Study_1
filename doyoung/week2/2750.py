import sys

lines = sys.stdin.read().split('\n')
# 입력받은 값은 문자열이므로 int로 치환, 첫번째 값은 총 데이터의 갯수이므로 제외
arr = list(map(int, lines[1:])) 
arr.sort()

for item in arr:
    print(item)


