A = int(input())
B = int(input())

n = B%10*A
nn = B%100//10*A
nnn = B%1000//100*A

print(n)
print(nn)
print(nnn)
print(n+nn*10+nnn*100)

#입력이 공백으로 주어진다면 map이나 split을 활용해도 되지만
#줄바꿈으로 표시된다면 각각 새로 정의해주어야 하나보다.