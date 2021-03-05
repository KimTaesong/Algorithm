# BOJ 11501 주식
T = int(input())  # 테스트케이스의 개수
for i in range(T):
    N = int(input())  # N: 자연수의 개수
    day_cost = list(map(int, input().split()))  # 날 별 주가
    print(N, day_cost)

"""
홍준 - 3가지 중 하나를 한다.
1. 주식 하나를 산다.
2. 원하는 만큼 가지고 있는 주식을 판다.
3. 아무것도 안한다.
target: 주어진 주가 정보를 가지고 최대 이익을 구해봐라.
"""


def hongjun_predict():
    pass
