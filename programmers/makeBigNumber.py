# def solution(number, k):
#
#     lng = len(number)
#     e = -(lng - k - 1)
#
#     b = list(map(lambda n : n, number))
#
#     answer = ''
#     idx = 0
#
#     iidx = 0
#     while True:
#         c_idx = 0
#         e_b = []
#
#         if (len(number) - idx == (-e + 1)):
#             answer += ''.join(b[idx:])
#             break
#
#         if e == 0 :
#             e_b = b[idx:]
#         else:
#             e_b = b[idx:e]
#         mm = 0
#         for i in range(len(e_b)):
#             c_i = int(e_b[i])
#             if c_i == 9:
#                 mm = c_i
#                 iidx = i
#                 break
#
#             if mm < c_i:
#                 mm = c_i
#                 iidx = i
#
#         idx += iidx + 1
#         e += 1
#
#         answer += str(mm)
#
#         if e > 0:
#             break
#
#     return answer

def solution(number, k):
    print(number)
    stack = [number[0]]

    print(stack)
    for num in number[1:]:
        print(num, stack[-1], k)
        while len(stack) > 0 and stack[-1] < num and k > 0:
            k -= 1
            stack.pop()
        stack.append(num)
        print('stack : ', stack)
    if k != 0:
        stack = stack[:-k]
    return ''.join(stack)
# print(solution("1924",2))
# print()
# print(solution("1231234",3))
# print()
# print(solution("4177252841",4))
print(solution("3191",2))
# a = [1,2,3,4,5,6,7,7,8]
# print(a[1:])
# b = a[1:]
# print(b)
# print(b.index(2))



