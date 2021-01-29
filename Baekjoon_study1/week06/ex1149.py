n = int(input())
painting_cost = [[0, 0, 0]]
dp_cost = [[0] * 3 for _ in range(n+1)]
for i in range(n):
    painting_cost.append(list(map(int, input().split())))

for i in range(3):
    dp_cost[1][i] = painting_cost[1][i]

for i in range(2, n+1):
    dp_cost[i][0] = painting_cost[i][0] + min(dp_cost[i-1][1], dp_cost[i-1][2])
    dp_cost[i][1] = painting_cost[i][1] + min(dp_cost[i-1][0], dp_cost[i-1][2])
    dp_cost[i][2] = painting_cost[i][2] + min(dp_cost[i-1][0], dp_cost[i-1][1])

print(min(dp_cost[n]))
