# BOJ 11501 주식
T = int(input())  # 테스트케이스의 개수
for i in range(T):
    N = int(input())  # N: 자연수의 개수
    day_cost = list(map(int, input().split()))  # 날 별 주가
    print(N, day_cost)
