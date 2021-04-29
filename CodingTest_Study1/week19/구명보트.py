def solution(people, limit):
    cnt = 0
    people.sort()

    left_pointer = 0
    right_pointer = len(people) - 1

    while left_pointer < right_pointer:
        if people[left_pointer] + people[right_pointer] <= limit:
            cnt += 1
            left_pointer += 1
        right_pointer -= 1

    return len(people) - cnt
