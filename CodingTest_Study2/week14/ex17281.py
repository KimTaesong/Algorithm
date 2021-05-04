import sys
input = sys.stdin.readline
def dfs(k):
    global result
    # 02. 타자 순서 결정 완료 - 1) 게임 진행 2) 최대 점수 갱신
    if k == 9:
        start, score = 0, 0

        for i in baseball:
            out, b1, b2, b3 = 0, 0, 0, 0

            while out <= 2:
                p = select[start]
                if i[p] == 0:
                    out += 1

                elif i[p] == 1:
                    score += b3
                    b1, b2, b3 = 1, b1, b2

                elif i[p] == 2:
                    score += (b2 + b3)
                    b1, b2, b3 = 0, 1, b1

                elif i[p] == 3:
                    score += (b1+ b2+ b3)
                    b1, b2, b3 = 0, 0, 1

                elif i[p] == 4:
                    score += (b1 + b2 + b3 + 1)
                    b1, b2, b3 = 0, 0, 0

                start += 1
                start %= 9

        result = max(result, score)
        return

    # 01. 백트래킹으로 선수단의 순서를 정함 - 8! 35000 < 대략 4만개의 조합 < 48000
    for i in range(9):
        if visited[i]:
            continue
        visited[i] = 1
        select[i] = k
        dfs(k+1)
        visited[i] = 0
        select[i] = 0

n = int(input())
baseball = [list(map(int, input().split())) for _ in range(n)] # 각 이닝별 타자들의 활약
select, visited = [0] * 9, [0] * 9 # 선수단의 조합, 방문 배열
select[3], visited[3] = 0, 1 # 4번타자는 무조건 1번 선수로 고정
result = 0 # 최대 타점
dfs(1)
print(result)
    

