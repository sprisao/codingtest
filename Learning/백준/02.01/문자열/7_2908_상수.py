A, B = list(map(int, input().split()))

nA= int(''.join(reversed(str(A))))
nB= int(''.join(reversed(str(B))))
if nA > nB:
  print(nA)
else:
  print(nB)
