
food_times = list(map(int , input().split()))

k = int(input())
zeroCount = 0
index = 0
while True :
    foodIndex = index % len(food_times)

    time = food_times[foodIndex]

    if time <= 0 :
        zeroCount += 1
        index += 1
        continue
    else:
        k -= 1
        food_times[foodIndex] = time - 1

    if k == -1:
        print(foodIndex + 1)
        break
    else :
        index += 1
    if zeroCount == len(food_times):
        print(-1)
        break



