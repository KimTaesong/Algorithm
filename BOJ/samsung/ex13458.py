import sys
input = sys.stdin.readline
n = int(input())  # 시험장의 개수
test_people = list(map(int, input().split()))
# b: 총 감독관이 감시할 수 있는 응시자 수, c: 부감독관 감시할 수 있는 응시자 수
b, c = map(int, input().split())
total_supervisor = 0  # 총 감독관의 수
for i in test_people:
    if i // b >= 1:
        i -= b
        total_supervisor += 1
        if i % c == 0:
            total_supervisor += i // c
        else:
            total_supervisor += i // c + 1
    else:
        total_supervisor += 1
print(total_supervisor)
