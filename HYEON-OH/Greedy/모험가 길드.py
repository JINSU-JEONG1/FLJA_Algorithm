# 아이디어 공포도가 낮은 인원들 부터 구성 하면서 최대한의 그룹을 만들도록 유도

n = int(input())
fear = list(map(int,input().split()))
 
fear.sort()
count = 0 # 현재 그룹에 포함된 모험가의 수
result = 0 # 그룹 수
 
for i in fear:
  count += 1 
  if count >= i: # 현재 그룹에 포함된 모험가의 수가 현재 확인하고 있는 공포도보다 크거나 같다면
    result += 1 # 그룹 결성
    count = 0 # 새로운 그룹 만들기 위해 그룹에 포함된 모험가의 수 초기화
 
print(result)