# BOJ 십자카드 2659
# 시계수를 찾는 함수: ex) 입력: abcd 시계방향으로 읽으면 bcda, cdab, dabc
def find_clocknum(num):
    clock_num = num
    for i in range(3):
        # 시계방향으로 자리수 갱신 bcda -> cdab -> dabc
        num = (num % 1000) * 10 + num // 1000
        if clock_num > num:  # 기존 시계수보다 작으면 새로 갱신
            clock_num = num
    return clock_num


number = find_clocknum(int(''.join(input().split())))

i = 1111
cnt = 0
# 몇 번째로 작은 시계수인지를 찾는 과정
while(i <= number):
    if find_clocknum(i) == i:  # 시계수를 찾는 함수와 값이 동일한 경우에만
        cnt += 1
    i += 1
print(cnt)
