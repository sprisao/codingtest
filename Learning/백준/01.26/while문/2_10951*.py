
# try와 except를 사용할 수 있다.


while True:
    try:
        A, B = map(int, input().split())
        print(A+B)
    except:
        break
