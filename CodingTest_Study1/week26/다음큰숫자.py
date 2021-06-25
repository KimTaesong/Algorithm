def solution(n):
    # 1의 개수를 저장 bin(n) 함수의 결과는 str
    one_cnt = bin(n).count('1')
    for i in range(n+1, 1000001):
        if one_cnt == bin(i).count('1'):
            return i
