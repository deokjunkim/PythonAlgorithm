def solution(number, k):
    count = len(number) -k
    print(count)
    answer = ''
    print(number[0:-3])
    print(number[2:])
    # while True:
    #     maxNum = 0
    #     idx = 0
    #     for n in number[idx : ]:
    #         idx += 1
    #         if maxNum < n:
    #             maxNum = n



    return answer





# solution("1924",2)
# print()
# solution("1231234",3)
# print()
# solution("4177252841",4)

# k = 2
a = [1,9,2,4]
print(a[:-1])
# k = 1 - 1
a1 = [2, 4]
print(a1[:0])
print()
b = [1,2,3,1,2,3,4]
print(b[0:-(7-5)])
b1 = [1,2,3,4]
print(b1[:-(4-(4-2+1))])
b2 = [4]
print(b2[:0])
# -( len - ( len - k +1 ))
-(1-1)

if( k == 0) 일때를 확인ㅛㅅ '해서 조건문 작성

