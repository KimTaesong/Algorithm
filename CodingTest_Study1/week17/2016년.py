def solution(a, b):
    day = ["THU", "FRI", "SAT", "SUN", "MON", "TUE", "WED"]
    cnt = b
    for i in range(1, a):
        if i == 1 or i == 3 or i == 5 or i == 7 or i == 8 or i == 10:
            cnt += 31

        elif i == 4 or i == 6 or i == 9 or i == 11:
            cnt += 30

        elif i == 2:
            cnt += 29
    print(cnt)
    print(day[cnt % 7])
    return day[cnt % 7]


solution(5, 24)
