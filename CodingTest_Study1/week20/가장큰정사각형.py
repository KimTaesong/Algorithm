# # 시간 초과 코드 - 완전 탐색
# def solution(board):
#     w = len(board)
#     h = len(board[0])

#     def dfs(x, y, n):
#         for i in range(x, x+n):
#             for j in range(y, y+n):
#                 if board[i][j] == 0:
#                     return False
#         return True


#     for i in range(min(w,h), 0, -1):
#         for j in range(w-i+1):
#             for k in range(h-i+1):
#                 if dfs(j, k, i):
#                     return i * i
# dp를 활용한 풀이
def solution(board):
    w = len(board[0])
    h = len(board)
    for x in range(1, h):
        for y in range(1, w):
            if board[x][y] == 1:
                board[x][y] = min(
                    board[x-1][y-1], min(board[x-1][y], board[x][y-1])) + 1
    max_num = 0
    for line in board:
        max_num = max(max(line), max_num)
    return max_num ** 2
