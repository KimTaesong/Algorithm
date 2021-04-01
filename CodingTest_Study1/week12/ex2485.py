# BOJ 가로수 2485
N = int(input())  # 가로수의 수
tree = [int(input()) for _ in range(N)]  # 가로수를 저장하는 배열
tree.sort()  # 가로수가 순서대로 입력되는게 아니기 때문에 정렬
tree_distance = [tree[i+1] - tree[i] for i in range(N-1)]  # 가로수 간 간격을 저장하는 배열

gcd_distance = tree_distance[0]


def gcd(a, b):
    return b if a % b == 0 else gcd(b, a % b)


# 모든 가로수 간 거리의 최대공약수를 간격으로 잡는다.
# why? ex) 2, 4, 6 - > 2
#      ex) 2, 3, 10 -> 최소값을 기준으로 하면 간격이 일정하지 않다.
for i in range(N-2):
    tmp = gcd(tree_distance[i], tree_distance[i+1])
    gcd_distance = gcd(gcd_distance, tmp)


distance = max(tree) - min(tree)  # 가장 멀리 떨어져 있는 두 가로수의 차이
# 가로수의 개수 : (거리) // (가로수 간 간격) + 1 - N (기존에 심어져 있는 가로수)
print(distance // gcd_distance + 1 - N)
