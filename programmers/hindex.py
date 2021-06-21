
def solution(ciations):
    ciations.sort()

    l = int(len(ciations)/2)
    for i in range(ciations[l], -1 , -1):
        sum = 0
        for j in ciations:
            if j >= i:
                sum += 1
            if sum >= i:
                return i


print(solution([3, 0, 6, 1, 5, 2]))