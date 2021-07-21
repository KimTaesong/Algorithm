from collections import deque
from collections import defaultdict


def solution(begin, target, words):
    # 2개의 단어가 서로 한글자만 다른 단어인지 판별
    def available(w1, w2):
        wrong = 0
        for i in range(len(w1)):
            if w1[i] != w2[i]:
                wrong += 1
            if wrong > 1:
                return False
        return True
    # BFS로 탐색하면서 가장 처음 target가 일치할 때,
    # 그때의 깊이가 구하고자 하는 결과 값(가장 짧은 변환 과정의 길이)이다.

    def bfs(word):
        queue = deque([[word, 0, []]])
        print(queue)
        while queue:
            print(queue)
            cur = queue.popleft()
            depth = cur[1]          # 현재 노드의 깊이 정보를 가져온다.
            path = cur[2]           # 현재 경로에 대한 정보를 가져온다.
            print(
                f"cur: {cur[0]}, target: {target},  de pth: {depth}, path: {path}")

            if cur[0] == target:    # target을 찾으면 depth 리턴 후 종료
                return depth

            print(words)
            # words 중 현재 경로 내엣 중복되지 않으면서 한 글자만 다른 단어(노드)를 선택
            for w in words:
                if available(cur[0], w):
                    print(f"cur: {cur[0]}, w: {w}, path: {path}")
                    if w not in path:   # 경로 내에서주는 중복되는 노드가 없도록
                        # 깊이, 경로 정보 갱신 후 전달
                        queue.append([w, depth + 1, path + [w]])
        return 0

    if target not in words:
        return 0

    return bfs(begin)


begin = ["hit", "hit"]
target = ["cog", "cog"]
words = [["hot", "dot", "dog", "lot", "log", "cog"]	,
         ["hot", "dot", "dog", "lot", "log"]]

for i in range(2):
    print(solution(begin[i], target[i], words[i]))
