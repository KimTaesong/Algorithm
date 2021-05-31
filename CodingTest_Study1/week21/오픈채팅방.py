def solution(record):
    uid_stack = {}
    name_stack = []
    for i in record:
        tmp = i.split()
        if len(tmp) == 2:
            command, uid = tmp[0], tmp[1]
            # print(command, uid)
            name_stack.append([uid, 0])

        elif len(tmp) == 3:
            command, uid, name = tmp[0], tmp[1], tmp[2]
            # print(command, uid, name)
            if command == "Enter":
                uid_stack[uid] = name
                name_stack.append([uid, 1])

            elif command == "Change":
                uid_stack[uid] = name

        # print(uid_stack)
        # print(name_stack)

    answer = []
    for i in name_stack:
        if i[1]:
            answer.append(uid_stack[i[0]] + "님이 들어왔습니다.")

        elif i[1] == 0:
            answer.append(uid_stack[i[0]] + "님이 나갔습니다.")

    return answer
