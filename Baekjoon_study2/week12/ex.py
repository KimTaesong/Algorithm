T = int(input())
for i in range(T):
    operations = input().split()
    cnt = float(operations[0])
    for j in operations[1:]:
        if j == '@':
            cnt *= 3
        elif j == '%':
            cnt += 5
        elif j == '#':
            cnt -= 7
        else:
            print("예외가 발생했습니다.")
    print(f"{cnt:.2f}")
