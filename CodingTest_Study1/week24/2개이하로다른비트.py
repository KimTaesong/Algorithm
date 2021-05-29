def solution(numbers):
    answer = []

    for number in numbers:
        # 파이썬 내장함수 bin -> ex) 숫자 2를 이진수로 변환 bin(2) -> 0b10 -> 슬라이싱으로 bin(2)[2:] -> 10
        # 값을 변환해주기 위해서 문자열을 리스트로 변환, 0을 붙여주는 이유는 자리수가 올라가는 경우를 대비하기 위해서
        bin_number = list('0' + bin(number)[2:])
        # bin 함수의 결과값은 문자열
        # print(type(bin_number))
        # find vs rfind -> find는 앞(왼쪽)부터, rfind는 뒤(오른쪽)에서부터 값을 찾음
        idx = ''.join(bin_number).rfind('0')
        # 00, 01, 10 -> 01, 10, 11 / 11의 경우 다름 뒤에서부터 처음 만나는 0을 1로 바꾸고 처음 만나는 0 뒤의 1값을 0으로 변경
        bin_number[idx] = '1'

        if number % 2 == 1:
            bin_number[idx+1] = '0'

        print(''.join(bin_number))
        # int(s, 2) int() 내장함수로 2진수 s를 10진수로 변환
        answer.append(int(''.join(bin_number), 2))
    return answer


print(solution([2, 7, 8, 10]))
