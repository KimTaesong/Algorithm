cnt = 0
for _ in range(int(input())):
    word = input()
    flag = False
    for i in range(len(word)-1):
        if word[i] == word[i+1]:
            continue

        if word[i] in word[i+1:]:
            flag = True
            break

    if not flag:
        cnt += 1
print(cnt)
