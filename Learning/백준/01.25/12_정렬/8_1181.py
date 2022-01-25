N = int(input())
d = dict()
# 같은 단어가 여러번 입력된 경우에는 한번씩만 출력한다. => dict를 사용하라는 힌트다.


for _ in range(N):
    word = input()
    d[word] = len(word)

candi = []

for k, v in d.items():
    candi.append([v, k])

candi.sort()


# 파이썬에서는 List내의 첫번재 Element의 값을 지정해서 뽑아낸다. -> Javascript랑 다른부분!!
for x, y in candi:
    print(y)
