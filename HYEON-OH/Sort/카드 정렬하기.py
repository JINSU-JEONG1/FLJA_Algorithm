# 데큐 힙큐 사용법
# from collections import deque
# import heapq



import heapq

n = int(input())


priorityQue = []

for i in range(n):
    num = int(input())
    heapq.heappush(priorityQue , num)


result = 0

if len(priorityQue) == 1:              ## while len(priorityQue) != 0 : 여기를 1 아닐때로 헀으면 더깔끔하게 풀수있었음
    result = 0
else:
        
    while len(priorityQue) != 0 :       ## 여기를 0 아닐때 말고 1 아닐때로 했을때 더 깔끔하게 풀수있음
        if len(priorityQue) == 1:
            num = heapq.heappop(priorityQue)
            result += num
            break
        num1 = heapq.heappop(priorityQue)
        num2 = heapq.heappop(priorityQue)

        result += num1 + num2

        if len(priorityQue) == 0:        ## 1 아닐때로 하고 풀면 조건 필요가 없어짐
            break

        heapq.heappush(priorityQue , num1 + num2)

print(result)