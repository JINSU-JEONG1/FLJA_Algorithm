# 내 아이디어 이진탐색으로 수 찾고 그수의 왼쪽 오른쪽을 탐색한다.
# 위에거는 틀렸다 N 탐색하게되서
# 리얼 아이디어는 첫번째 x의 위치와 마지막 x의 위치를 알아서 뺴서 개수 알아내는 식으로 해야 함!


# N개의 원소를 포함하고 있는 수열이 오름차순으로 정렬되어있습니다. 이때 이수열에서 x가 등장 하는 횟수를 계산하세요. 예를 들어 수열 {1,1,2,2,2,2,3} 이 있을때 x = 2 라면, 현재 수열에서 값이 2 인 원소가 4개 이므로 4를  출력합니다.

# 단, 이문제는 시간복잡도 O(logN)으로 알고리즘을 설계하지 않으면 '시간초과 '판정을 받습니다.

# 입력조건
# 첫째줄에 N과 x가 정수형태로 공백으로 구분되어 입력됩니다. (1 <= N <= 1000000) , (-10의9승 <= x <= 10의9승)
# 둘째줄에 N개의 원소가 정수 형태로 공백으로 구분되어 입력됩니다. (-10의9승 <= 각 원소의 값 <= 10의9승)

# 출력조건
# 수열의 원소중에서 값이 x인 원소의 개수를  출력 합니다. 단, 값이 x인 원소가 하나도 없다면 -1을 출력합니다.


# n , x = map(int, input().split())

# list = list(map(int , input().split()))

# start = 0 
# end = len(list)-1
# count = 0
# targetIndex = -1
# while start <= end :
#     mid = (start + end ) // 2
#     if x == list[mid]:
#         count += 1
#         targetIndex = mid    
#         break
#     elif list[mid] > x:
#         end = mid - 1
#     elif list[mid] < x:
#         start = mid + 1

# if targetIndex != -1:
#     searchPlusIndex = mid + 1
#     while searchPlusIndex < len(list) and list[searchPlusIndex] == x:
#         count += 1
#         searchPlusIndex += 1

#     searchMinusIndex = mid -1

#     while searchMinusIndex >= 0 and list[searchMinusIndex] == x:
#         count += 1 
#         searchMinusIndex -= 1


#     print(count)
# else :
#     print(-1)
######## 위에 답은 오답입니다 ########



# 이진탐색의 조건 종류 start < end ///// start <= end
# 조건3개로 분류 mid == x , mid > x , mid < x
# 조건2개로 분류 mid >= x , mid < x ////// mid > x , mid <= x 
# mid 만 넣는 경우  mid +- 1 해서 넣는경우 


#결국에 반반씩 하게되면 start == end 가 되기 때문에
# start, end = 0, len(a)   # [start, end)
# while start < end:
# 반으로 나눌때 둘중에 하나는 mid 만 줘도됨
# start, end = 0, len(a)-1 # [start, end]
# while start <= end:
# 반으로 나눌때 둘중 어느것도 min 만 주면 무한 루프 돌수 있음



# first x 와 last x 를구하는 방법은
# 정렬 배열에서 x의 맨 아래(첫 위치) / **맨 위(마지막 위치)**는 이진탐색을 “어느 쪽으로 계속 좁히느냐”로 결정돼.
# 핵심은 이거 2개:
# 첫 x (lower_bound): x를 만나도 왼쪽으로 더 간다
# 마지막 x (upper_bound-1): x를 만나도 오른쪽으로 더 간다

# 마지막에 end 를 리턴해야 되나 start 를 리턴해야되나 헤깔리는데
# 오른쪽으로 조이면 마지막에 start에 +1 하자너 그래서 end 리턴
# 왼쪽으로 조이면 마지막에 end에 +1 해서 start 리턴 하면됨
def getLastX(array , x) :
    start = 0
    end = len(array) -1
    while start <= end :
        mid = (start + end) // 2

        if array[mid] > x :
            end = mid -1
        elif array[mid] <= x:
            start = mid + 1

    if array[end] == x:
        return end
    else :
        return -1



def getFirstX(array , x) :
    start = 0
    end = len(array) -1
    while start <= end :
        mid = (start + end) // 2

        if array[mid] >= x :
            end = mid -1
        elif array[mid] < x:
            start = mid + 1

    if array[start] == x:
        return start
    else :
        return -1








n , x = map(int, input().split())

list = list(map(int , input().split()))

getLastX(list , x)

