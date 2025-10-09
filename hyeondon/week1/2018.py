import sys

num = int(sys.stdin.readline())

data = [i for i in range(1, num+1)]  
left, right = 0, 0
current_sum = data[0]
count = 0

while right < num:
    if current_sum == num:
        count += 1
        current_sum -= data[left]
        left += 1   
    elif current_sum < num:
        right += 1
        if right < num:
            current_sum += data[right]
    else:
        current_sum -= data[left]
        left += 1

print(count)
