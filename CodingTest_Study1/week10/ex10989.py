#BOJ 수 정렬하기 3 10989
# 메모리 제한이 있어서 그냥 for문 돌려서 append해준 후 정렬을 하면 틀리는 문제.
# c나 java처럼 크기가 정해진 배열을 만들고 nums 배열의 index에 개수를 저장해줌 
# for문으로 인덱스에 저장된 수만큼 출력을 해주고 인덱스가 0이면 그냥 지나침.
import sys
N = int(sys.stdin.readline())
nums = [0] * 10001

for _ in range(N):
    nums[int(sys.stdin.readline())] += 1

for k in range(10001):
    if nums[k] != 0:
        for j in range(nums[k]):
            print(k)