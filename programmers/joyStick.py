def solution(name):

    change = [ord(n) - ord('A') if ord(n) <= ord('N') else ord('Z') - ord(n) + 1 for n in name]

    idx = 0
    answer = 0
    print(change)
    while True:
        answer += change[idx]
        change[idx] = 0
        if sum(change) == 0:
            return answer

        left, right = 1, 1

        while change[idx - left] == 0:
            left += 1

        while change[idx + right] == 0:
            right += 1

        answer += left if left < right else right
        idx += -left if left < right else right


    return  answer





# print('A')-int('B'))
# print(ord('A') - ord('Z'))
solution("JEROEN")
# solution("JAN")
# print(ord('Z') - ord('N'))
# print(chr(ord('Z') - ord('N') + 1))
# print(ord('N') - ord('A'))
# print(ord('A'), ord('Z'), ord('N'))
# a = dict('a','b')
# print(a)
