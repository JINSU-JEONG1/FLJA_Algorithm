#for i in range(y, -1, -1):
#     ...
# 설명:
# range(start, stop, step)
# stop은 포함 안 됨이라서 0까지 포함하려면 stop을 -1로 둬야 해.

def isDirectionLog(x,y,direction):
    for i in visited[x][y]:
        if i == direction:
            return True
    
    return False

def searchWithDirection(map , x , y , n, visited):
    # 오른쪽으로 먼저 탐색
    for i in range(y+1 , n):
        if map[x][i] == "T":
            if isDirectionLog(x,i , "L") :
                continue
            else:
                visited[x][i].append("L")
                break

    #왼쪽으로 탐색
    for i in range(y-1 , -1 , -1):
        if map[x][i] == "T":
            if isDirectionLog(x,i , "R") :
                continue
            else:
                visited[x][i].append("R")
                break

    #아래로 탐색
    for i in range(x+1 ,n):
        if map[i][y] == "T":
            if isDirectionLog(i,y , "U") :
                continue
            else:
                visited[i][y].append("U")
                break

    
    # 위로 탐색        
    for i in range(x-1 , -1 , -1):
        if map[i][y] == "T":
            if isDirectionLog(i,y , "D") :
                continue
            else:
                visited[i][y].append("D")
                break








n = int(input())


visited = [[ [] for _ in range(n) ] for _ in range(n) ]



map = []

for i in range(n):
    map.append(input().split())


for x in range(n):
    for y in range(n):
         if map[x][y] == "S" :
             searchWithDirection(map , x , y , n , visited)
    

count = 0
for visitedRow in visited :
    for visitedArray in visitedRow:
        count += len(visitedArray)


if count <= 3:
    print("YES")
else:
    print("NO")