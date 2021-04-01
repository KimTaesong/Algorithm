# BOJ 정수론 및 조합론 최대공약수와 최소공배수 2609
a, b = map(int, input().split())

# for i in range(1, min(a, b)+1):
#     if a % i == 0 and b % i == 0:
#         gcd_value = i

# for i in range(min(a, b), 0, -1):
#     if a % i == 0 and b % i == 0:
#         gcd_value = i
#         print(i)
#         break


def gcd(a, b):
    return b if a % b == 0 else gcd(b, a % b)


print(gcd(a, b))
print(a*b//gcd(a, b))
