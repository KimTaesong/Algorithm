#BOJ 1406 에디터
import sys

words = list(sys.stdin.readline())
N = len(words)
M = int(sys.stdin.readline())
pointer = N


def check(com: str):
    global pointer
    if com[0] == 'P':
        words.insert(pointer, com[1])
        pointer += 1

    elif com[0] == 'L':
        if pointer != 0:
            pointer -= 1

    elif com[0] == 'D':
        if pointer != len(words):
            pointer += 1

    elif com[0] == 'B':
        if pointer != 0:
            words.pop(pointer-1)
            pointer -= 1 

    else:
        print(f"예외문자 {com}가(이) 입력되었습니다.")


for i in range(M):
    command = sys.stdin.readline().split()
    check(command)

for k in words:
    print(k, end='')
