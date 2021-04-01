# BOJ 숫자 고르기 2668
n = int(input())
dic = {}
for i in range(n):
    dic[i+1] = int(input())

while True:
    baseSet = set(dic.values())
    dic = {key: value for key, value in dic.items() if key in baseSet}
    if baseSet == set(dic.values()):
        break
print(len(dic))
for key in dic.keys():
    print(key)
