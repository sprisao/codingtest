def get_hansu_num(N):
  if N < 100:
    hansu = N
    #99이하는 차이라고 할 만한 수가 하나씩밖에 나오지 않음으로 모두 한수다.
    #따라서 한수는 99개다.
  else:
    hansu = 99
    #N이 100을 넘어간다면 일단 한수는 99개부터 시작한다.
    #그 이후 100부터 한수인지 아닌지 검사한뒤 맞을경우 한수에 값을 1씩 추가하는 함수를 정한다.

    for i in range(100, N+1):
      num_list = list(map(int, str(i)))
      if num_list[0] - num_list[1] == num_list[1] - num_list[2]:
        hansu += 1
        
  return hansu

if __name__ == "__main__":
  input_num = int(input())

  print(get_hansu_num(input_num))
