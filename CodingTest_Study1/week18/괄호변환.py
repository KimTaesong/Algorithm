def is_right(s):
    flag = 0
    for i in s:
        if i == '(':
            flag += 1
        else:
            flag -= 1
        if flag < 0:
            return False
    return True


def reverse(s):
    tmp = ''
    for i in s:
        if i == '(':
            tmp += ')'
        else:
            tmp += '('
    return tmp


def solution(p):
    if p == '':
        return ''

    flag = 0
    for i in range(len(p)):
        if p[i] == '(':
            flag += 1
        else:
            flag -= 1

        if flag == 0:
            u = p[:i+1]
            v = p[i+1:]
            break

    if is_right(u):
        print("균형잡힌 괄호 문자열")
        return u + solution(v)

    return '(' + solution(v) + ')' + reverse(u[1:-1])
