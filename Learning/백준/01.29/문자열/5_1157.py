S = input().casefold()

d=dict()
for i in S:
  if i in d:
    d[i] += 1
  else:
    d[i] = 1

result=[]
for k, v in d.items():
  if max(d.values()) == v:
    result.append(k)

if len(result) > 1:
  print('?')
else:
  print(result[0].upper())