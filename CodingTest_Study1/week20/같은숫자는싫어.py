def solution(arr):
    n = len(arr)
    tmp = [arr[0]]
    for i in range(n-1):
        if arr[i] != arr[i+1]:
            tmp.append(arr[i+1])

    return tmp


arr = [[1, 1, 3, 3, 0, 1, 1], [4, 4, 4, 3, 3]]
for i in range(len(arr)):
    print(solution(arr[i]))
