# successCount challengeCount 구할때 이중포문으로 돌면은 못품
# 아래처럼 누적합을 이용 풀이 ㄱㄱ 



def solution(N, stages):
    successCount = [0]*(N+2)
    challengeCount = [0]*(N+2)
    stuckCount = [0] * (N+2)
    
    for challenge in stages:
        stuckCount[challenge] += 1
    
    
    runningCount = stuckCount[N+1]
    for i in range(N , 0 , -1):
        runningCount += stuckCount[i]
        challengeCount[i] = runningCount
        successCount[i] = runningCount - stuckCount[i]
    
    
    
    probability = [0] * (N+1)
    answer = []
    
    for stage in range(1 , N+1):
        answer.append(stage)
        if challengeCount[stage] == 0:
            probability[stage] = 0
            continue
        
        pro = (challengeCount[stage] - successCount[stage]) / challengeCount[stage]
        probability[stage] = pro
        
    
    answer.sort(key=lambda x : (-probability[x] , x))
    
    
    return answer