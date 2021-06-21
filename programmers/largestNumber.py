import functools

def comparator(a,b):
    print(a, b)
    t1 = a+b
    t2 = b+a
    print((int(t1) > int(t2)) - (int(t1) < int(t2)))
    return (int(t1) > int(t2)) - (int(t1) < int(t2)) #  t1이 크다면 1  // t2가 크다면 -1  //  같으면 0

def solution(numbers):
    n = [str(x) for x in numbers]
    n.sort(reverse= True)
    answer = ''
    print(n)
    for i in n:
        answer += "".join(i)

    return answer


solution([6, 10, 2])
solution([3, 30, 34, 5, 9])




