# BOJ 예산 2529
import sys
input = sys.stdin.readline
k = int(input())
symbol = list(input().split())
nums = []
visited = [0] * 10
for i in range(10 ** (k-1), 10 ** (k+1)):
    if i < 10 ** k:
        string = '0' + str(i)
    else:
        string = str(i)

    flag = True

    for i in range(k+1):
        if visited[int(string[i])] == 0:
            visited[int(string[i])] = 1
        else:
            flag = False
            break
    for j in range(k):
        if flag and symbol[j] == '>' and int(string[j]) > int(string[j+1]):
            pass
        elif flag and symbol[j] == '<' and int(string[j]) < int(string[j+1]):
            pass
        else:
            flag = False
            break

    if flag:
        nums.append(string)
    visited = [0] * 10
print(nums[-1])
print(nums[0])
