# BOJ 요세푸스 문제 1158
N, K = map(int, input().split())  # N명의 사람, K: 제거할 인덱스
people = [i for i in range(1, N+1)]
pointer = 0
yosepus_array = []
while people:
    pointer = (pointer + (K-1)) % len(people)
    yosepus_array.append(people.pop(pointer))

for i in range(N):
    if N == 1:
        print("<%d>" % yosepus_array[i])
    else:
        if i == 0:
            print("<%d" % yosepus_array[i], end=', ')
        elif i == N-1:
            print("%d>" % yosepus_array[i])
        else:
            print(yosepus_array[i], end=', ')

"""
0 1 2 3 4 5 6
1 2 3 4 5 6 7

pointer = (K -1) % len(a)
pointer = 2
a.pop(pointer) = 3

0 1 2 3 4 5 
1 2 4 5 6 7

pointer += (K-1)
pointer = pointer % len(a)
a.pop(pointer)

pointer = 2 + (K-1) = 4
a.pop(pointer) = 6

0 1 2 3 4
1 2 4 5 7

0 1 2 3
1 4 5 7

0 1 2
1 4 5

0 1
1 4

0
1

None

pop()을 하는 순간-> 1 2 4 5 6 7 인덱스 값이 바뀌는 문제점: 그러면 K-1칸 이동
pointer의 값은 3 (K-1)
1 2 4 5 7
"""
