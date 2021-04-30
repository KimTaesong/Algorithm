def solution(number, k):
    stack = [number[0]]
    for num in number[1:]:
        # 스택과 K > 0, stack 마지막 요소 num보다 작을 경우 반복
        while len(stack) > 0 and k > 0 and stack[-1] < num:
            k -= 1
            stack.pop()  # stack의 마지막 요소를 재거
        stack.append(num)  # stackdp num 추가

    if k > 0:  # k가 0보다 클 경우
        stack = stack[:-k]  # stack을 뒤에서부터 k만큰 제외

    return ''.join(stack)
