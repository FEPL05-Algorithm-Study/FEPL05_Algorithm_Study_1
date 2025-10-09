import sys

input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
arr.sort()


# 좋은 수 판별
def double_pointer(index, target, data_list):
    start, end = 0, len(data_list) - 1  # 양쪽 끝 번호 저장

    while start < end:
        # 본인과 똑같은 index면 건너 뜀
        if index == start:
            start += 1
            continue

        if index == end:
            end -= 1
            continue
        
        sum = data_list[start] + data_list[end]

        # 비교후에 끝낼건지 왼쪽, 오른쪽 더 탐색할건지 비교
        if target == sum:
            return True
        elif target > sum:
            start += 1
        else:
            end -= 1
        
    return False
    

result = 0

for i, item in enumerate(arr) :
    if double_pointer(i, item, arr):
        result += 1
    
    
print(result)

