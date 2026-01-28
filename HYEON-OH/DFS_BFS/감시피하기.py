#for i in range(y, -1, -1):
#     ...
# 설명:
# range(start, stop, step)
# stop은 포함 안 됨이라서 0까지 포함하려면 stop을 -1로 둬야 해.
from itertools import combinations

def watch(map, x, y, n):
    # 선생 (x,y)에서 학생이 보이면 True
    # O 만나면 그 방향 중단
    # X는 통과
    # T는 통과해도 되지만 보통 상관없음(여기선 그냥 통과 처리)
    # U
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