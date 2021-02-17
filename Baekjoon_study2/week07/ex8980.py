# BOJ 택배 8980
N, C = map(int, input().split())  # N: 마을 수, C: 트럭의 용량
M = int(input())  # M: 박스 정보의 개수
for i in range(M):
    # 박스를 보내는 마을번호, 박스를 받는 마을번호, 보내는 박스의 개수
    start_city, dest_city, postbox_cnt = map(int, input().split())
    print(start_city, dest_city, postbox_cnt)
print(N, C, M)
