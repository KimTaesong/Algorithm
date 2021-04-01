# BOJ 스택 잃어버린 괄호 1541
cal_word = input().split('-')
cnt = 0
for i in range(len(cal_word)):
    word = list(map(int, cal_word[i].split('+')))
    if i == 0:
        cnt += sum(word)
    else:
        cnt -= sum(word)
print(cnt)
