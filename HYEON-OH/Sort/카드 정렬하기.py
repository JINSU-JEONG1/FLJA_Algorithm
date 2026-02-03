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

if len(priorityQue) == 1:
    result = 0
elif len(priorityQue) == 2:
    num1 = heapq.heappop(priorityQue)
    num2 = heapq.heappop(priorityQue)
    result = num1 + num2
else:
        
    while len(priorityQue) != 0 :
        if len(priorityQue) == 1:
            num = heapq.heappop(priorityQue)
            result += num
            break
        num1 = heapq.heappop(priorityQue)
        num2 = heapq.heappop(priorityQue)

        result += num1 + num2

        if len(priorityQue) == 0:
            break

        heapq.heappush(priorityQue , num1 + num2)

print(result)