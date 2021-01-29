# BOJ 그리디 ATM 11399
N = int(input())  # 사람의 수
bank_cost = list(map(int, input().split()))  # 은행에서 기다리는 사람들의 소요 시간
bank_cost.sort()  # 오름차순으로 정렬 시켜서 소요시간이 적은 사람순으로 업무 처리하면 가장 최소

cnt = 0
tmp = 0

for i in bank_cost:
    tmp += i
    cnt += tmp
print(cnt)
