# 2진수
# bin()
# 8진수
# oct()
# 16진수
# hex()

# 다른 진법의 수를  10진수로 변환 하는 프로그램 작성
# 1. 해당 값이 2진수, 8진수, 16진수 인지 파악하기
# 2.
#def two_Binary():

num = 1001
base = 2
print(num % 10)
print(int(num / 10))
result, multiple = 0,1
while num > 0:
    n = num % 10
    value = n * multiple
    multiple *= base
    num = int(num / 10)
    result += value
    print(n, int(multiple/2), result)

print(result)

