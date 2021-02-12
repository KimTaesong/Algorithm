# BOJ 촌수 계산 2644
n = int(input())  # 전체 사람 수 n
A, B = map(int, input().split())  # 촌수 계산하는 사람 2명
m = int(input())  # 부모 자식들 간의 관계의 개수 m
graph = [0] * (n+1)  # 부모 자식 관계를 저장하는 그래프

for i in range(m):
    x, y = map(int, input().split())  # x 부모, y 자식
    graph[y] = x

Aa, Ba = [], []
Ad, Bd = 0, 0
while A > 0:
    Aa.append((A, Ad))
    Ad += 1
    A = graph[A]

while B > 0:
    Ba.append((B, Bd))
    Bd += 1
    B = graph[B]


for i in Aa:
    for j in Ba:
        if i[0] == j[0]:
            print(i[1]+j[1])
            exit()
print(-1)
