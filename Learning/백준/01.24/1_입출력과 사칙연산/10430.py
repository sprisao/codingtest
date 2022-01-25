# 입력 : 첫째 줄에 A, B, C가 순서대로 주어진다. (2 ≤ A, B, C ≤ 10000)

# A,B,C = input().split()
# A = int(A)
# B = int(B)
# C = int(C)

A, B, C = map(int, input().split())

print((A+B) % C)
print(((A % C)+(B % C)) % C)
print((A*B) % C)
print(((A % C)*(B % C)) % C)
