# BOJ 중복 빼고 정렬하기 10867
N = int(input())  # N개의 정수가 주어짐.
nums = list(map(int, input().split()))
unique_nums = []
for i in nums:
    if i not in unique_nums:
        unique_nums.append(i)
sorted_unique_nums = sorted(unique_nums)

for k in sorted_unique_nums:
    print(k, end=' ')
