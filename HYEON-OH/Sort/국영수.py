n = int(input())
list = []
for i in range(n):
    name, guk, young, su = input().split()
    list.append((name,int(guk),int(young),int(su)))

list.sort(key=lambda x : (-x[1] , x[2] , -x[3] , x[0]))


for i in list:
    print(i[0])

