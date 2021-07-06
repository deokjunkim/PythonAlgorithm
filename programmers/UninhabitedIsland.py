def solution(people, limit):
    people.sort()
    cnt = 0
    i = 0
    j = len(people) - 1

    while i <=j:
        print(i, people[i], j, people[j])
        cnt +=1
        if people[i] + people[j] <= limit:
            i += 1
        j -= 1

    return cnt

# solution([70, 50, 80, 50], 100)
# solution([70, 80, 50], 100)
print(solution([50, 40, 50, 60], 100))

# a = [1,2,3]
# print(a[0:])