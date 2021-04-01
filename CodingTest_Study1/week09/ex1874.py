# BOJ 1874 스택 수열
n = int(input())
target = [int(input()) for _ in range(n)]  # 입력된 수열
origin = []
operation = []
i = 1
cnt = 0

while i <= n or origin:
    # print(f"i: {i}")
    # print(f"cnt: {cnt}")
    # print(f"origin: {origin}")
    # print(f"operation: {operation}")
    if i < target[cnt]:
        origin.append(i)
        operation.append('+')
        i += 1

    elif i == target[cnt]:
        origin.append(i)
        operation.append('+')
        origin.pop()
        operation.append('-')
        cnt += 1
        i += 1

    elif i > target[cnt]:
        if origin[-1] != target[cnt]:
            print("NO")
            exit()
        else:
            origin.pop()
            operation.append('-')
            cnt += 1


for k in operation:
    print(k)
