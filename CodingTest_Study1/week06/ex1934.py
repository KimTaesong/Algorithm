# BOJ 정수론 및 조합론 최소공배수 1934
t = int(input())
for i in range(t):
    a, b = map(int, input().split())
    if b > a:
        a, b = b, a
    L = a * b
    while(b != 0):
        a = a % b
        a, b = b, a
    print(L//a)
