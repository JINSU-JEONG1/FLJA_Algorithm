#for i in range(y, -1, -1):
#     ...
# 설명:
# range(start, stop, step)
# stop은 포함 안 됨이라서 0까지 포함하려면 stop을 -1로 둬야 해.

# 문제 풀면서 고생 했던점 
# 선생에서 학생을 보는 관점으로 해야지 
# 학생에서 선생을 보는 관점으로 하니까 애초에 존나 힘들었음
# 관건은 선생이 봤을때 학생이 없어야 하는거니까 애초에 이렇게 생각 했으면 좀더 쉽게 갈수 있었음
# 학생이 봤을때 선생의 관점은 결국 너무 어려운 선택이 였음 애초에 완탐이면 문제에서 알려주는 핵심에 가까운 생각으로 시작 할수 있도록 해야함!!!





from itertools import combinations

def watch(map, x, y, n):
    for i in range(x - 1, -1, -1):
        if map[i][y] == "O":
            break
        if map[i][y] == "S":
            return True
    # D
    for i in range(x + 1, n):
        if map[i][y] == "O":
            break
        if map[i][y] == "S":
            return True
    # L
    for j in range(y - 1, -1, -1):
        if map[x][j] == "O":
            break
        if map[x][j] == "S":
            return True
    # R
    for j in range(y + 1, n):
        if map[x][j] == "O":
            break
        if map[x][j] == "S":
            return True

    return False


n = int(input())
tPositions = []
combiList = []
map = []

for i in range(n):
    map.append(input().split())

for x in range(n):
    for y in range(n):
        if map[x][y] == "T":
            tPositions.append((x, y))
        elif map[x][y] == "X":
            combiList.append((x, y))

result = False

for com in combinations(combiList, 3):
    # 장애물 설치
    for i in com:
        map[i[0]][i[1]] = "O"

    bad = False
    for t in tPositions:
        if watch(map, t[0], t[1], n):
            bad = True
            break

    # 원복
    for i in com:
        map[i[0]][i[1]] = "X"

    if not bad:
        result = True
        break

if result:
    print("YES")
else:
    print("NO")