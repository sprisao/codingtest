cro_alp = list(['c=', 'c-','dz=','d-','lj', 'nj', 's=', 'z='])

S = input()

count = 0 
for i in cro_alp:
  if i in S:
    count += S.count(i)
    S = S.replace(i,' ')

S = S.replace(' ', '')
print(len(S) + count)