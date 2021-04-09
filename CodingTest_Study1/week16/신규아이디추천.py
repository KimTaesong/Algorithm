def solution(new_id):
    # 1. 아이디의 길이는 3 <= len <= 15
    # 2. 아이디는 소문자, 숫자, '-', '_', '.' 문자만 사용 가능
    # 3. '.'의 경우 처음과 끝에 사용 불가, 연속으로 사용 불가
    # 1단계 대문자 -> 소문자
    new_id = new_id.lower()
    print(new_id)
    # 2단계 소문자, 숫자, '-', '_', '.' 제외한 모든 문자를 제거.
    tmp = ''
    for i in new_id:
        if i.isalnum() or i == '-' or i == '_' or i == '.':
            tmp += i
    new_id = tmp
    print(new_id)
    # 3단계 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환합니다.
    tmp = ''
    for i in range(len(new_id)-1):
        if new_id[i] == new_id[i+1] == '.':
            continue
        tmp += new_id[i]

    if new_id[-1] != '.':
        tmp += new_id[-1]

    else:
        tmp += '.'

    new_id = tmp
    print(new_id)
    # 4단계 new_id에서 마침표(.)가 처음이나 끝에 위치한다면 제거합니다.
    if len(new_id) == 1 and new_id[0] == '.':
        new_id = ''

    elif len(new_id) >= 2 and new_id[0] == '.':
        new_id = new_id[1:]

    if new_id and new_id[-1] == '.':
        new_id = new_id[:-1]

    print(new_id)
    # 5단계 new_id가 빈 문자열이라면, new_id에 "a"를 대입합니다.
    if new_id == '':
        new_id = 'a'
    print(new_id)
    # 6단계 new_id의 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거합니다.
    # 만약 제거 후 마침표(.)가 new_id의 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거합니다.
    if len(new_id) >= 16:
        new_id = new_id[:15]
        if new_id[-1] == '.':
            new_id = new_id[:14]
    print(new_id)
    # 7단계 new_id의 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙입니다.
    if len(new_id) <= 2:
        l = len(new_id)
        tmp = new_id[-1]
        for i in range(3-l):
            new_id += tmp
    print(new_id)

    answer = new_id
    return answer


new_id = ["...!@BaT#*..y.abcdefghijklm", "z-+.^.",
          "=.=", "123_.def", "abcdefghijklmn.p"]
for i in range(len(new_id)):
    solution(new_id[i])
