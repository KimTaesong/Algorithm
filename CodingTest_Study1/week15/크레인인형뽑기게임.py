def solution(board: list, moves: list):
    # board 2차원 리스트, moves 1차원 리스트
    transport_board = []
    stack = []
    answer = 0

    for i in range(len(board)):
        temp_list = []
        for j in range(len(board)-1, -1, -1):
            temp_list.append(board[j][i])
        transport_board.append(temp_list)
    print(transport_board)

    for k in moves:
        for p in range(len(board)-1, -1, -1):
            if transport_board[k-1][p] != 0:
                stack.append(transport_board[k-1][p])
                transport_board[k-1][p] = 0
                break

        if len(stack) > 1:
            if stack[-1] == stack[-2]:
                stack.pop()
                stack.pop()
                answer += 2
    return answer
