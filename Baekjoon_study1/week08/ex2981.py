# BOJ 정수론 및 조합론 검문 2981
N = int(input())  # 종이에 적은 수의 개수 N
math_note = []  # 수학 게임에 사용할 숫자
answer_note = []
a = 0
b = 0
for i in range(N):
    math_note.append(int(input()))


def gcd(a, b):
    return b if a % b == 0 else gcd(b, a % b)


math1_note = [abs(math_note[k] - math_note[k+1])
              for k in range(len(math_note)-1)]
if len(math1_note) == 1:
    a = math1_note[0]
else:
    for j in range(len(math1_note)-1):
        if j == 0:
            a = math1_note[j]
            b = math1_note[j+1]
            a = gcd(a, b)
        else:
            b = math1_note[j+1]
            a = gcd(a, b)

for i in range(2, (a // 2) + 1):
    if a % i == 0:
        print(i, end=' ')
print(a)
