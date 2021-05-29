def solution(s):
    trans_cnt = 0       # 이진 변환 횟수
    del_zero_cnt = 0    # 0을 제거한 횟수
    string = list(s)    # 문자열 조작을 하기 위해 리스트로 변환

    # 이진 변환 과정
    while True:
        trans_cnt += 1
        del_zero_cnt += string.count('0')  # count를 이용해 제거할 0의 개수를 더함

        if len(string) - string.count('0') == 1:  # 0 제거 후 길이가 1이면 이진 변환 중단
            break
        string = list(bin((len(string) - string.count('0')))
                      [2:])  # 0 제거 후 길이를 이진수로 변환

    return [trans_cnt, del_zero_cnt]
