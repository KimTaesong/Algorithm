# BOJ 연속합 1912
n = int(input())
nums = [0] + list(map(int, input().split()))  # 입력받은 숫자 배열
dp = [-1000] * (n+1)  # 연속합을 저장하는 dp배열
# 이전 연속합 + 해당 인덱스값 vs 해당 인덱스 값을 비교해서 큰 값을 저장
dp[1] = nums[1]
for i in range(2, n+1):
    dp[i] = max(nums[i], dp[i-1] + nums[i])
# 연속합 배열의 합 중 가장 큰 값을 출력
print(max(dp))
