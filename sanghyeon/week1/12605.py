n=int(input()) # 테스트 케이스 개수 n을 입력

for i in range(n): # n번 범위 반복
	n_list = list(input().split()) 
	n_list = n_list[::-1] # 슬라이싱 스텝 -1로 리스트 뒤집기
	s = ' '.join(n_list) # 리스트를 문자열로 변환
	print("Case #%d: %s" %(i+1, s))