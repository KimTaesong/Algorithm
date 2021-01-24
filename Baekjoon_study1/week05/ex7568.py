# BOJ 브루트포스 덩치 7568
N = int(input())
rating = []  # 사람들의 덩치 순위를 저장할 배열
people = []  # 사람들의 키와 몸무게를 저장하는 배열
for i in range(N):
    weight, height = map(int, input().split())  # 몸무게, 키
    people.append([weight, height])  # 배열 형태로 몸무게, 키를 저장

# 전수 조사 i번째 사람과 j번째 사람의 키와 몸무게를 비교
for i in range(N):
    flag = [False, False]  # 덩치가 크다는 것을 체크하는 배열, [0]번째 인덱스 몸무게, [1]번째 인덱스 키
    rate = 1
    for j in range(N):
        flag[0] = True
        flag[1] = True
        for k in range(2):
            if i != j:
                if people[i][k] < people[j][k]:
                    flag[k] = False
        if flag[0] == flag[1] == False:  # 둘 다 False이면 i번째 사람이 j번째 사람보다 덩치가 작다는 것을 의미
            rate += 1  # 순위를 증가
    rating.append(rate)

for _ in rating:
    print(_, end=' ')
