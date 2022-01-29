S = str(input())

a = "abcdefghijklmnopqrstuvwxyz"

alp_list = list(a)

#### 아스키 코드로 알파벳은 요렇게 표현한다는거
# alp_list = list(range(97,123)) 
for i in alp_list:
  print(S.find(i), end = ' ') ##### <- 연속해서 보이도록

#find() 함수 

