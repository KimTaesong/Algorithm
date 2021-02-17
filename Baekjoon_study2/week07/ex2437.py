# BOJ 2437 저울
N = int(input())  # 저울추의 개수
weights = list(map(int, input().split()))  # 저울추 배열
max_value = sum(weights)
combi = [0]
dp = [0] * (max_value+1)
for i in range(1, max_value+1):  # 1~ max_value 값까지 조사
    pass
    if i != sum(combi[i]):  # 부분집합의 합이 i와 같지 않은 경우에 값을 출력하고 브레이크로 탈출
        print(i)
        break
