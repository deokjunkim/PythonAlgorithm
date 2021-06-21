def solution(array, commands):
    answer = []

    for com in commands:
        i = com[0]
        j = com[1]
        k = com[2]
        answer.append(sorted(array[i-1:j])[k-1])
    return answer

solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]])

