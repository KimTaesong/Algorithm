def solution(lottos, win_nums):
    answer = []
    total_cnt = 0
    zero_cnt = 0
    for i in range(len(lottos)):
        if lottos[i] == 0:
            zero_cnt += 1
        else:
            if lottos[i] in win_nums:
                total_cnt += 1
    min_rank = 0
    if total_cnt <= 1:
        min_rank = 6
    else:
        min_rank = 7- total_cnt
    
    if total_cnt + zero_cnt <= 1:
        max_rank = 6
    else:
        max_rank = 7 - total_cnt - zero_cnt
    
    return [max_rank, min_rank]