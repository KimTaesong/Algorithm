# BOJ 정수론 및 조합론 링 3036
N = int(input())  # 링의 개수 N
ring = list(map(int, input().split()))  # 링의 모음


def gcd(a, b):
    return b if a % b == 0 else gcd(b, a % b)  # 최대공약수를 구하기 위한 유클리드 호제법


for i in range(1, len(ring)):  # 기약 분수로 표현하기 위해서 첫번째링과 각각의 링의 최대공약수를 나눠줘야 함
    first_ring = ring[0] // gcd(ring[0], ring[i])
    other_ring = ring[i] // gcd(ring[0], ring[i])
    print(f"{first_ring}/{other_ring}")
