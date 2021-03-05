# BOJ 1,2,3 더하기 9095
T = int(input())  # 테스트 케이스의 개수 T가 주어짐
sum_list = []
for i in range(T):
    n = int(input())
    sum_list.append(n)


def oneTwoThreeSum(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 4
    else:
        return oneTwoThreeSum(n-3) + oneTwoThreeSum(n-2) + oneTwoThreeSum(n-1)


for k in sum_list:
    print(oneTwoThreeSum(k))
