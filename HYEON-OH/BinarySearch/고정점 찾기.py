# 고정점 이란, 수열의 원소중에서 그값이 인덱스와 동일한 우너소를 의미합니다. 예를들어 수열 a = {-15,-4,2,8,13}이 있을떄 a[2] = 2 이므로 고정점은 2가 됩니다.
# 하나의 수열이 N개의 서로다른 원소를 포함하고 있으며, 모든원소가 오름차순으로 정렬되어있습니다. 이떄 수열에서 고정점이 있다면 , 
# 고정점을 출력하는 프로그램을 작성하세요 고정점은 최대 1개만 존재합니다. 만약 고정점이 없다면 -1을 출력합니다.
# 단, 이문제는 시간복잡도 O(logN)으로 알고리즘을 설계하지 않으면 시간초과 판정을 받습니다.
# 입력조건
# 첫째줄에 N이 입력됩니다. (1<= N <= 1000000)
# 둘째줄에 N개의 원소가 정수형태로 공백으로 구분되어 입력됩니다. (-10의9승 <= 각 원소의 값 <= 10의9승)
# 출력조건
# 고정점을 출력한다. 고정점이 없다면 -1을 출력합니다.

# 내 아이디어 -> 고정점을 빨리 찾을수있는 방법이 뭐가있을까 이미 수열은 정렬이 되어있는상태 0 의 값하고 N-1 값의 위치를 구할까? 구한다음에 그인덱스가 0 ~ N-1 안에 들어가는 값이 있는경우 탐색 없는경우 거시기 로직 ㄱㄱ



def findFirstIndex(array , x):
    start = 0
    end = len(array) - 1

    while start <= end :
        mid = (start + end) // 2

        if array[mid] >= x:
            end = mid -1
        if array[mid] < x:
            start = mid + 1

    if start >= 0 and start <= len(array) - 1 and array[start] >= x :
        return start
    else:
        return -1



        
def findLastIndex(array , x):
    start = 0
    end = len(array) - 1

    while start <= end :
        mid = (start + end) // 2

        if array[mid] > x:
            end = mid -1
        if array[mid] <= x:
            start = mid + 1

    if end >= 0 and end <= len(array) - 1 and array[end] <= x :
        return end
    else:
        return -1








n = int(input())

array = list(map(int , input().split()))


firstIndex = findFirstIndex(array , 0)

lastIndex = findLastIndex(array , n -1)
result = 0

if firstIndex != -1 and lastIndex != -1 :
    for i in range(firstIndex , lastIndex +1):
        if array[i] == i :
            result = i
            break
    
if result == 0 :
    print(-1)
else :
    print(result)
         

