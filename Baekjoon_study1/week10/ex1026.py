# BOJ 1026 보물찾기
N = int(input()) 
A = list(map(int, input().split())) # A 배열
B = list(map(int, input().split())) # B 배열 - 재배열 금지
cnt = 0 # 총 합을 저장하는 변수

for k in range(N):
    cnt += A.pop(A.index(min(A))) * B.pop(B.index(max(B)))

print(cnt)