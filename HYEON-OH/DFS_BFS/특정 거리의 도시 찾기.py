# “둘 다 []를 복사하는 거잖아?” → 포인트는 “[]를 여러 개 만들었냐”야
# 1번 [[]] * (n+1) : 리스트 1개 만들고, 참조를 n+1번 반복
# 2번 [[] for _ in range(n+1)] : 리스트를 n+1개 새로 만들어 넣음
#
# 1. 그니까 [ 내용 ] * 내용을몇개복사   *는 리스트 안의 값을 복사하는 기능 참조 복사 
#
# 2. 그래서 lst = [표현식 for _ in range(N)]
# a = [0 for _ in range(5)]     # [0,0,0,0,0]
# b = ['x' for _ in range(3)]   # ['x','x','x']

n , m , k , x = map(int , input().split())

graph = [[] for _ in range(n+1)]

minGraph = [300001] * (n+1)

result = []


for _ in range(m):
    first , second = map(int , input().split())
    graph[first].append(second)

def dfs(k, start , graph , minGraph , content):
    if(content > k):
        return
    
    for i in graph[start]:
        minGraph[i] =  min(minGraph[i] , content+1)
        dfs(k , i , graph , minGraph , content+1)

dfs(k, x ,graph ,minGraph,0 )

count = 0
for i in range(n+1):
    if minGraph[i] == k:
        count += 1
        print(i)

if count == 0:
    print(-1)



#dfs 로하면은 풀수가 없음 간선 비용이 다 1 일때는 최초 도착하는 노드비용이 최단 거리 이기때문에 이지점에 분기처리를 해서 bfs 로 로직 의 이득을 취해야한다 중요!