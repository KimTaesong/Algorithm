# BOJ 2504 괄호의 값 - 미해결(Runtime Error)
# 예외 테스트케이스를 못 찾겠음.
stack = []
string = input()
answer = 0
for i in string:
    if i == '(' or i == '[':
        stack.append(i)
        # print(stack)

    elif i == ')':
        if stack:
            if stack[-1] == '(':
                stack.pop()
                stack.append(2)

            elif stack[-1] == '[':
                print(0)
                exit()

            elif type(stack[-1]) == int:
                cnt = 0
                while stack:
                    if stack[-1] != '(':
                        cnt += stack.pop()
                    else:
                        break
                if stack:
                    stack.pop()
                    stack.append(cnt * 2)

                else:
                    print(0)
                    exit()

            # print(stack)
        else:
            print(0)
            exit()

    elif i == ']':
        if stack:
            if stack[-1] == '[':
                stack.pop()
                stack.append(3)

            elif stack[-1] == '(':
                print(0)
                exit()

            elif type(stack[-1]) == int:
                cnt_1 = 0
                while stack:
                    if stack[-1] != '[':
                        cnt_1 += stack.pop()
                    else:
                        break
                if stack:
                    stack.pop()
                    stack.append(cnt_1 * 3)

                else:
                    print(0)
                    exit()

            # print(stack)

        else:
            print(0)
            exit()

while stack:
    if stack[-1] == '(' or stack[-1] == '[':
        print(0)
        exit()
    else:
        answer += stack.pop()
print(answer)
