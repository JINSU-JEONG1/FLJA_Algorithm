# n = int(input())
# numList = list(map(int , input().split()))

# numList.sort()
# minSum = 99999999999999
# minI = 0

# for i in numList:
#     sum = 0
#     for j in numList:
#         sum += abs(j - i)
#     if sum < minSum:
#         minI = i
#         minSum = sum
        
# print(minI)


## 오답








#답은 그냥 중간 찌르기
n = int(input())
numList = list(map(int , input().split()))

numList.sort()
print(numList[(n-1) // 2])