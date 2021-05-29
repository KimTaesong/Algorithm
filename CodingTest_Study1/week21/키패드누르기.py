def solution(numbers, hand):
    answer = ''
    left = [3, 0]
    right = [3, 2]

    for i in numbers:
        if i % 3 == 1:
            answer += 'L'
            left = [i//3, 0]

        elif i > 0 and (i % 3 == 0):
            answer += 'R'
            right = [i//3 - 1, 2]

        elif i == 2 or i == 5 or i == 8 or i == 0:
            if i == 0:
                i = 11

            pos = [i // 3,  1]
            left_move = abs(left[0] - pos[0]) + abs(left[1] - pos[1])
            right_move = abs(right[0] - pos[0]) + abs(right[1] - pos[1])

            if left_move > right_move:
                right = pos
                answer += 'R'

            elif left_move < right_move:
                left = pos
                answer += 'L'

            elif left_move == right_move:
                if hand == "right":
                    right = pos
                    answer += 'R'

                elif hand == "left":
                    left = pos
                    answer += 'L'
    return answer
