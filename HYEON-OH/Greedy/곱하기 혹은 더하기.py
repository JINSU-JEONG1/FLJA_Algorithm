# 더하거나 곱하는 수가 1 이나 0 이 없을경우에는 다곱하고 나머지경우 다 더한다.


numbers = list(map(int , input()))



result = 0

if len(numbers) == 1:
    print(numbers[0])
elif len(numbers) >= 2:
    result = numbers[0]
    for i in range(1 , len(numbers)) :
        if result <= 1 or numbers[i] <= 1:
            result += numbers[i]
        else:
            result *= numbers[i]





print(result)