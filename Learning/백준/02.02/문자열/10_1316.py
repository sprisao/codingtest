N = int(input())

count = N

for i in range(N):
  S = input()
  w =[]
  for j in range(0, len(S)-1):
    if S[j]==S[j+1]:
      pass
    elif S[j] in S[j+1:]:
      count -= 1
      break
print(count)


#문자열에서 특정값이 연속해서 나올경우 하나로 카운팅
# 꼭 연속해서 나오지 않더라도 단독적으로 나올경우 ok
#이후 연속되지 않지만 같은 문자가 나올경우에는 false <-- 결국, 이 조건만 충족하는지 알 수 있다면 해결가능

# 1. 기존에 이미 나온 문자 ? 
# 2. 연속해서 나오지 않음
# 3. find() 클래스를 통해 위치를 리스트로 넘겨받고
# 4. for 문으로 리스트의 마지막 값보다 큰값이 있을경우 -> 이건 연속문자가 아니다.

