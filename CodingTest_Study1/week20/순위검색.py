# https://bladejun.tistory.com/71?category=426398

import bisect


def make_cases(idx):
    global changes, temp
    if idx == 4:
        new = []
        for i in temp:
            new.append(i)
        changes.append(new)
        return

    for i in (False, True):
        temp.append(i)
        make_cases(idx+1)
        temp.pop()


def search(scores, num):
    size = len(scores)
    return size - bisect.bisect_left(scores, num, lo=0, hi=size)


def solution(info, query):
    global changes, temp
    answer = []    # 정답
    changes = []   # True, False 저장
    temp = []       # DFS를 위한 임시 리스트
    dic = {}  # key:정보, value:score

    # DFS를 통해 changes 배열 채워넣기
    make_cases(0)

    # query를 위한 info 전처리
    for data in info:
        data = data.split()
        score = int(data[-1])
        data = data[:4]

        for change in changes:
            # 데이터 복제 -> 원본 데이터 유지
            _data = [x for x in data]

            # change배열에 따라서 True -> '-' / False -> 원본데이터 변경
            _data = ['-' if change[i] else _data[i] for i in range(4)]

            # 한줄로 이어붙여서 dictionary key로 사용
            _data = ''.join(_data)

            # key를 정보 value를 score
            # 중복될 경우를 대비해서 value를 list로 저장
            if _data not in dic.keys():
                dic[_data] = [score]
            else:
                dic[_data].append(score)

    # info_dict[key] 정렬
    # -> 정렬을 해주는 이유는 나중에 binary tree를 사용하기 위해서이다!
    for key in dic.keys():
        dic[key].sort()

    for q in query:
        q = q.split()
        score = int(q[-1])

        # query 문자열 처리
        string = ''.join([x for x in q[:-1] if x != 'and'])

        # binary search tree를 사용해 정답 구하기
        if string in dic.keys():
            cnt = search(dic[string], score)
            answer.append(cnt)
        else:
            answer.append(0)

    return answer


info = ["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150",
        "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100", "python and frontend and senior and chicken 200",
         "cpp and - and senior and pizza 250", "- and backend and senior and - 150", "- and - and - and chicken 100", "- and - and - and - 150"]
print(solution(info, query))
