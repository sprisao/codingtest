S = input()

D = [('ABC', 2), ('DEF', 3), ('GHI',4), ('JKL',5), ('MNO',6), ('PQRS', 7), ('TUV',8),('WXYZ',9)]
count = 0

#문자의 조합이 특정 문자를 포함하고 있을때 v값 찾기
for chr in str(S):
  for couple in D:
    if chr in couple[0]:
      count += int(couple[1]+1)

print(count)