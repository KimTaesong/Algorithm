# BOJ 코딩테스트 6603 로또
import itertools

while True:
    testcase = list(map(int, input().split()))
    if testcase[0] == 0:
        break
    combination = list(itertools.combinations(testcase[1:], 6))
    for i in combination:
        for j in i:
            print(j, end=' ')
        print()
    print()
