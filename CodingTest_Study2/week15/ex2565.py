line = int(input())
AB_line = []

for _ in range(line):
    A, B = map(int, input().split())
    AB_line.append([A,B])

#A오름차순으로 정렬
AB_line = sorted(AB_line, key = lambda x: x[0])


#LIS를 구해주자
result = [[] for _ in range(line)]
for i in range(line):
    if i == 0:
        result[i].append(AB_line[i][1])
    else:
        for j in range(0, i):
            if result[j][-1] < AB_line[i][1]:
                if len(result[i]) - 1 < len(result[j]):
                    result[i] = result[j] + [AB_line[i][1]]
        if not result[i]:
            result[i].append(AB_line[i][1])


#가장 긴 수열
maximum = 0
for i in range(line):
    maximum = max(maximum, len(result[i]))
print(line - maximum)