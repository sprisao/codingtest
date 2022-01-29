numbers = set(range(1, 10000))
remove_set = set()  # 생성자가 있는 숫자 set
for num in numbers :
    for n in str(num):
        num += int(n)
    remove_set.add(num)  # add: 집합에 요소를 추가할 때

self_numbers = numbers - remove_set  # set의 '-' 연산자로 차집합을 구함
for self_num in sorted(self_numbers):  # sorted 함수로 정렬
    print(self_num)

# 내가 여기서 잘 살펴보아야 할 부분은 무엇일까?
# 1. for문을 사용해서 리스트를 만들고 정의하는 방법
# 2. 함수를 만드는 것은 어떻게 하는건지 염두
# 3. set() 함수를 활용하여 일정 구간의 수들을 리ㄴ스트로 만드는 방법
# list()와 set() 클래스의 차이는 무엇일까?
# set은 요소들이 순서대로 저장되어 있지 않다.
# 따라서 for문에서 읽어들일때 무작위 순서로 나온다.
# 동일한 값의 요소가 1개 이상 존재할 수 없다.
# 새로 저장하려는 값이 포함 되어있는 값이라면 새로운 요소가 이 전 요소를 치환한.


################################### 아래는 내 오답
# for i in range (3):
#   n = i + 1
#   while True:
#     a = n // 10
#     b = n % 10
#     c = n + a + b
#     n = c 
#     if n > 100:
#       break
#     else:
#       print(c)


# while True:
#   a = n // 10
#   b = n % 10
#   c = n + a + b
#   print(c)
#   if c > 100:
#     break

