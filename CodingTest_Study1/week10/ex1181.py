#BOJ 단어정렬 1181
N = int(input()) # 단어의 개수
words = {}
for i in range(N):
    word = input()
    words[word] = len(word)

sorted_words = sorted(words.items(), key=lambda word: (word[1], word[0]))

for k in sorted_words:
    print(k[0])