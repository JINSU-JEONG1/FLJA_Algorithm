from collections import deque

t = int(input())

results = []
for i in range(t):
    n , m  = map(int, input().split())

    dp = [[0]*(m+2) for _ in range(n+2)]

    number =deque(list( map(int , input().split())))                                                                                                               
    grid = [[0]*(m+2) for _ in range(n+2)]


    for j in range(1,n+1):
        for h in range(1,m+1):
            grid[j][h] = number.popleft()

    
    for k in range(1 , n+1):
        dp[k][1] = grid[k][1]

    for column in range(2 , m+1): ## 2부터 해야됨 1은 이미 했으니꼐~~~
        for row in range(1 , n+1):
            dp[row][column] = max(dp[row-1][column-1] + grid[row][column] , dp[row][column-1] + grid[row][column] , dp[row+1][column-1] + grid[row][column])


    result = 0
    for number in range(1 , n+1):
        result = max(dp[number][m] , result)
    
    results.append(result)




for i in range(len(results)):
    print(results[i])