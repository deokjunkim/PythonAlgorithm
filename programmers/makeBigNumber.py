def solution(number, k):
    lng = len(number)
    e = -(lng - k - 1)
    b = list(map(lambda n : n, number))
    answer = ''
    idx = 0

    while True:
        c_idx = 0
        e_b = []

        if e == 0 :
            e_b = b[idx:]
        else:
            e_b = b[idx:e]

        if(len(number) - idx == (-e+1)):
            answer +=''.join(b[idx:])
            break

        m = max(e_b)

        c_idx = e_b.index(m) + 1
        idx = c_idx + idx 
        e += 1

        answer += m

        if e > 0:
            break

    return answer

print(solution("1924",2))
print()
print(solution("1231234",3))
print()
print(solution("4177252841",4))
# a = [1,2,3,4,5,6,7,7,8]
# print(a[1:])
# b = a[1:]
# print(b)
# print(b.index(2))



