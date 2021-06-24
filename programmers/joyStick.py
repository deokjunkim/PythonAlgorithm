def solution(name):
    answer = 0
    idx = 0
    Acount = 0
    bidx = 0
    for i in range(len(name)):
        if name[i] == 'A':
            for y in range(i,len(name)):
                if name[y] == 'A':
                    Acount += 1
                else:
                    break
    # left
    if Acount > len(name) - bidx:

    else:



    return answer





# print('A')-int('B'))
# print(ord('A') - ord('Z'))
# solution("JEROEN")
# solution("JAN")
print(ord('Z') - ord('N'))
print(chr(ord('Z') - ord('N') + 1))
print(ord('N') - ord('A'))