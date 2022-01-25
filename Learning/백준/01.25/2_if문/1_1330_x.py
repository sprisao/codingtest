# 문제
# 두 정수 A와 B가 주어졌을 때, A와 B를 비교하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 A와 B가 주어진다. A와 B는 공백 한 칸으로 구분되어져 있다.

# 출력
# 첫째 줄에 다음 세 가지 중 하나를 출력한다.

# A가 B보다 큰 경우에는 '>'를 출력한다.
# A가 B보다 작은 경우에는 '<'를 출력한다.
# A와 B가 같은 경우에는 '=='를 출력한다.
# 제한
# -10, 000 ≤ A, B ≤ 10, 000
# 예제 입력 1
# 1 2
# 예제 출력 1
# <
# =======================================================================
import sys
input = sys.stdin.readline

# int로 각각 분리해서 받을땐 map 을 사용해야되나보다.
A, B = map(int, input().split())
if A > B:
    print('>')
elif A < B:
    print('<')
else:
    print('==')

# print('>') if A > B else print('<') if A < B else print('==') 이런식으로도 가능하다.
