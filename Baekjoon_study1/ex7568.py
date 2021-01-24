N = int(input())
rating = []
people = []
for i in range(N):
    weight, height = map(int, input().split())  # 몸무게, 키
    people.append([weight, height])

for i in range(N):
    flag = [False, False]
    rate = 1
    for j in range(N):
        flag[0] = True
        flag[1] = True
        for k in range(2):
            if i != j:
                if people[i][k] < people[j][k]:
                    flag[k] = False
        if flag[0] == flag[1] == False:
            rate += 1
    rating.append(rate)

for _ in rating:
    print(_, end=' ')
