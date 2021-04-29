def solution(numbers: list, target: int):
    sub_list = [0]
    for i in numbers:
        temp_list = []
        for j in sub_list:
            temp_list.append(j+i)
            temp_list.append(j-i)
        sub_list = temp_list
    return sub_list.count(target)
