def solution(n, results):
    # wins[key] = key가 이긴 사람들의 잡합
    # loses[key] = key가 이기지 못한 사람들의 집합
    wins, loses = {}, {}
    for i in range(1, n+1):
        wins[i], loses[i] = set(), set()

    print(f"wins: {wins}")
    print(f"loses: {loses}")

    for i in range(1, n+1):
        for battle in results:
            print(f"i: {i}, battle: {battle}")
            if battle[0] == i:  # i의 승리. i가 이긴 사람들
                wins[i].add(battle[1])
            if battle[1] == i:  # i의 패배. i가 진 사람들
                loses[i].add(battle[0])
            print(f"wins:{wins}")
            print(f"loses: {loses[i]}")

        # i를 이긴 사람들 (loses[i]) => i에게 진 사람(wins[i])은 반드시 이긴다
        for winner in loses[i]:
            wins[winner].update(wins[i])

        # i에게 진 사람들 (wins[i]) => i를 이긴 사람들(loses[i])에게는 반드시 진다
        for loser in wins[i]:
            loses[loser].update(loses[i])

    cnt = 0
    for i in range(1, n+1):
        if len(wins[i]) + len(loses[i]) == n - 1:
            cnt += 1
    return cnt


print(solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))
