# BOJ 스택 괄호 9012
def vps_check(word):
    stack = []
    for i in word:
        if i == '(':
            stack.append(i)
        else:
            if stack:
                pop_word = stack.pop()
                if pop_word == '(':
                    pass
                else:
                    return "NO"
            else:
                return "NO"
    if stack:
        return "NO"
    else:
        return "YES"


T = int(input())
answer = []
for _ in range(T):
    testcase = input()
    answer.append(vps_check(testcase))
for i in answer:
    print(i)
