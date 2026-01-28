from collections import deque


def solution(p):
    w = list(p)


    answer = recursive(w)

    return ''.join(answer)




def recursive(w):
    result = []
    left = 0
    right = 0
    v = deque(w.copy())
    u = deque()
    for i in w:
        v.popleft()
        if i == "(":
            left += 1
            u.append(i)
        elif i == ")":
            right += 1
            u.append(i)
        else:
            return

        if left == right:
            break;

    if isRight(u) :
        result.extend(u)
        if len(v) == 0:
            result.extend([])
        else:    
            result.extend(recursive(v))
        return result
    else :
        u.pop()
        u.popleft()
        result.append("(")
        if len(v) == 0:
            result.extend([])
        else:    
            result.extend(recursive(v))
        result.append(")")
        result.extend(makeReverse(u))
        return result



def isRight(u):
    left = 0
    right = 0

    for i in u:
        if i == "(":
            left += 1
        elif i == ")":
            right += 1
        if right > left :
            return False

    return True


def makeReverse (u):
    newU = []
    for i in u :
        if i == "(":
            newU.append(")")
        elif i == ")":
            newU.append("(")

    return newU




#재귀를 생각할때 제귀호출 제일 끝부분과 제일 앞부분을 먼저 생각 하는 식으로 진행함