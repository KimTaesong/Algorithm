def solution(s):

    string_length = []  # 압축 문자열의 길이 저장
    result = ""

    if len(s) == 1:  # 문자열의 길이가 1이면 결과는 무조건 1
        return 1

    # 부분문자열의 길이가 1부터 문자열의 절반까지 자르며 비교해야하기 때문에
    for cut in range(1, len(s)//2 + 1):
        temp = s[:cut]  # 초기값 설정
        num = 1

        # 정해진 길이를 문자열 s의 길이까지 정해진 길이 스텝으로 반복
        for i in range(cut, len(s), cut):
            # temp값과 자른 문자열이 같은 경우
            if s[i:i+cut] == temp:
                # 부분 문자열의 개수
                num += 1
            # 다른 경우
            else:
                # 숫자가 1이면 문자열에 붙지 않으므로 제거
                if num == 1:
                    num = ""
                # 결과값에 숫자와 temp에 저장된 값을 저장
                result += str(num) + temp
                # temp값을 변경
                temp = s[i:i+cut]
                # 숫자 다시 초기화
                num = 1

        # else로 끝났을때만 저장이 되므로 반복
        if num == 1:
            num = ""

        result += str(num) + temp
        string_length.append(len(result))
        result = ""

    # 부분 문자열의 길이 최소값 반환
    return min(string_length)
