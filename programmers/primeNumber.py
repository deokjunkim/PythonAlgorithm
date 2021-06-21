from itertools import permutations
def solution(numbers):
    answer = 0
    a = []
    for n in numbers:
        a.append(n)

    s = set()
    for i in range(len(a),0,-1):
        for y in list(permutations(a,i)):
            c =''
            for j in y:
                c += "".join(j)
            s.add(int(c))

    for i in s:
        for y in range(2,i,1):
            if i%y == 0:
                break
            if i == y+1:
                answer +=1

    return answer

print(solution("17"))
print(solution("011"))


def prime_list(n):
    # 에라토스테네스의 체 초기화: n개 요소에 True 설정(소수로 간주)
    sieve = [True] * n
    print(sieve)
    # n의 최대 약수가 sqrt(n) 이하이므로 i=sqrt(n)까지 검사
    m = int(n ** 0.5)
    # print(int(m* 0.5))
    for i in range(2, m + 1):
        if sieve[i] == True:           # i가 소수인 경우
            for j in range(i+i, n, i): # i이후 i의 배수들을 False 판정
                sieve[j] = False

    # 소수 목록 산출
    return [i for i in range(2, n) if sieve[i] == True]

# print(prime_list(20))