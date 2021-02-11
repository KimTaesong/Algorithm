first_word = input()  # 첫번째 문자
second_word = input()  # 두번째 문자
first_length = len(first_word) + 1
second_length = len(second_word) + 1

lcs = [[0] * first_length for _ in range(second_length)]

for i in range(1, first_length):
    for j in range(1, second_length):
        if first_word[i-1] == second_word[j-1]:
            lcs[i][j] = lcs[i][j-1] + 1
        else:
            lcs[i][j] = max(lcs[i][j-1], lcs[i-1][j])
print(lcs[-1][-1])
