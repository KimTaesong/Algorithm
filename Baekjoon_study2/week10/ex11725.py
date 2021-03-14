# BOJ 11725 트리의 부모 찾기
N = int(input())  # 노드의 개수
tree = [0] * 100001
stack = []
for i in range(N-1):
    a, b = map(int, input().split())
    if a == 1:
        tree[b] = 1

    elif b == 1:
        tree[a] = 1

    elif tree[a]:
        tree[b] = a

    elif tree[b]:
        tree[a] = b

    else:
        stack.append([a, b])
for i in range(len(stack)):
    if tree[stack[i][0]]:
        tree[stack[i][1]] = stack[i][0]

    elif tree[stack[i][1]]:
        tree[stack[i][0]] = stack[i][1]

for i in tree[2:]:
    if i != 0:
        print(i)
