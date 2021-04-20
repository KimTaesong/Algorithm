import math
from itertools import permutations


def is_prime_number(n):
    """소수판별 함수"""
    if n == 0 or n == 1:                                # 0,1 은 소수가 아님
        return False
    else:
        # sqrt(n)까지만 for문을 돌면서 확인하면 된다.
        for i in range(2, int(math.sqrt(n)) + 1):
            # 2~sqrt(num)까지 나누어 떨어지는 숫자가 있으면 소수가 아님
            if n % i == 0:
                return False

        return True                                 # for문을 다 돌았는데도 False가 아니면 소수


def solution(numbers):
    answer = []
    for i in range(1, len(numbers)+1):
        # permutations(순열)을 사용해 i개씩 묶어지는 list 생성
        arr = list(permutations(numbers, i))
        for j in range(len(arr)):                   # 생성한 list(arr) 길이만큼 for문 실행
            # list(arr)의 값들은 tuple들로 되어있으모 join(map(str,))을 사용해 join해준다
            num = int(''.join(map(str, arr[j])))
            if is_prime_number(num):
                # is_prime_number() 함수가 True일 경우 (= 소수일 경우) num 추가
                answer.append(num)

    # 같은 값이 나올 수 있기 때문에 set()을 통해 중복값 제거
    answer = list(set(answer))
    return len(answer)
