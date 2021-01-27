n = int(input())  # 금액
coin_cnt = 0

coin_list = [500, 100, 50, 10]  # 동전의 종류

for i in coin_list:
    coin_cnt += n // i
    n %= i

print(coin_cnt)
