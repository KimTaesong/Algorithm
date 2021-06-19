from collections import deque
import sys
input = sys.stdin.readline

for i in range(int(input())):
    commands = input().strip()
    n = int(input())
    tmp = input()[1:-2].split(",")

    def check(coms, tmp):
        flag = False
        if tmp == ['']:
            for com in coms:
                if com == "D":
                    return "error"
            return []

        else:
            q = deque(list(map(int, tmp)))
            for com in coms:
                if com == "R" and q:
                    if flag == False:
                        flag = True
                    else:
                        flag = False

                elif com == "D" and q:
                    if flag:
                        q.pop()
                    else:
                        q.popleft()

                else:
                    return "error"
            if flag:
                q.reverse()
            return list(q)

    answer = check(commands, tmp)

    if answer == "error":
        print(answer)

    elif answer == []:
        print([])

    else:
        print("[", end="")
        for i in range(len(answer)):
            if i < len(answer)-1:
                print(answer[i], end=",")
            else:
                print(answer[i], end="]")
        print()
