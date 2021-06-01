# 기본수식
basic_formula = ['+', '-', '*']

# 간단한 계산을 해주는 함수


def calculator(a, b, p):
    if p == '*':
        return a * b
    if p == '+':
        return a + b
    return a - b


def make_priority(index, priority, visited, temp):
    # 마지막까지 왔다면 수식 추가
    if index == 3:
        priority.append(temp[:])
        return
    # 반복문을 돌면서 추가
    for i in range(3):
        if visited[i] == 0:
            visited[i] = 1
            temp.append(basic_formula[i])
            make_priority(index+1, priority, visited, temp)
            temp.pop()
            visited[i] = 0


def solution(expression):
    answer = 0
    # 끊은 데이터를 저장하기 위한 변수
    numbers = []
    formula = []
    # 어디를 끊었는지 기억하기 위한 변수
    slice_index = 0
    # 들어온 수식을 돌면서 슬라이싱
    for i in range(len(expression)):
        # 수식이 나온다면
        if expression[i] in basic_formula:
            # 숫자부분을 슬라이싱하여 numbers에 추가
            numbers.append(int(expression[slice_index:i]))
            # 수식부분을 formula변수에 추가
            formula.append(expression[i])
            # 다음시작은 i 뒤부터
            slice_index = i+1
    # 제일 마지막은 수식이 없으므로 따로 처리
    numbers.append(int(expression[slice_index:]))

    # 수식 우선순위 구하기
    priority = []
    # dfs형식을 이용하기 위해 방문여부 체크
    visited = [0, 0, 0]
    # 수식 우선순위 구하기
    make_priority(0, priority, visited, [])
    print(priority)

    # 총 가지수가 6번이므로 3번 반복
    for pri in priority:
        temp_numbers = numbers[:]
        temp_formula = formula[:]
        # 수식은 3가지이므로 3번 반복
        for p in pri:
            i = 0
            # i가 수식의 길이보다 짧을때까지 반복
            while(i < len(temp_formula)):
                # 우선순위 수식과 같다면
                if temp_formula[i] == p:
                    # 번호를 추출
                    a = temp_numbers[i]
                    # 계산하면 사라지므로 pop
                    b = temp_numbers.pop(i+1)
                    # 계산한 값을 넣어주기
                    temp_numbers[i] = calculator(a, b, p)
                    # 사용한 수식 제거
                    temp_formula.pop(i)
                    # 수식을 제거했으므로 인덱스 감소
                    i -= 1
                # 인덱스 증가
                i += 1
        # 남아있는 값이 최대값보다 크다면 갱신
        if abs(temp_numbers[0]) > answer:
            answer = abs(temp_numbers[0])
    return answer
