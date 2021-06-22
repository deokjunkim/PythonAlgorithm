def solution(brown, yellow):
    answer = []
    min = 2000000
    for y in range(yellow,0, -1):
        # print(yellow, y, int(yellow % y))
        if(yellow % y == 0 ):
            m = int(yellow / y)
            # print(yellow, y, int(yellow/y))
            # print(min, m, y, abs(m-y), answer)
            if min > abs(m-y):
                min = abs(m-y)
                # if y >= m:
                if (2*y) + (2*m) + 4 == brown:
                    return  [y + 2, m + 2]
                # else:
                #     answer = [m + 2, y + 2]

    #         print()
    # print('===================================================')

    return answer

print(solution(10, 2))	#[4, 3]
print('===================================================')
print()
print(solution(8,	1))	    #[3, 3]
print('===================================================')
print()
print(solution(24, 24))	#[8, 6]
print('===================================================')


print(24**(1/2)+1)
print(24**2)