def solution(phone_book):
    answer = True
    phone = {}  # 딕셔너리 형태

    # 전화번호부를 딕셔너리형으로 저장
    for i in phone_book:
        phone[i] = 1

    for k in phone_book:
        tmp = ""
        # 전화번호부의 번호 하나씩 조사 ex) k : 110 num: 1, 1, 0순으로 조사
        for num in k:
            tmp += num
            # 일부가 전화번호부 번호에 포함되면 answer flag를 False 변경
            if tmp in phone and tmp != k:
                answer = False
                return answer
    return answer
