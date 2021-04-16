import math

def testing_fibonacci():
    fibonacci = [1,1]
    count = 0
    while count < 10:
        length = len(fibonacci)
        print(fibonacci[length-1], fibonacci[length-2])
        fibonacci.append(fibonacci[length-1]+ fibonacci[length-2])
        count += 1
    print(fibonacci)

def find_fibonacci_seq_iter(n):
    if n < 2: return n
    a, b = 0 , 1
    for i in range(n):
        a, b = b, a + b
    print(a)
    return a

def find_fibonacci_seq_rec(n):
    if n<2: return n
    return  find_fibonacci_seq_rec(n-1) + find_fibonacci_seq_rec(n-2)

def find_fibonacci_seq_form(n):
    sq5 = math.sqrt(5)
    phi = (1+sq5) /2
    return int(math.floor(phi ** n / sq5))

if __name__ == "__main__":
    # testing_fibonacci()
    n = 10
    find_fibonacci_seq_iter(n)
    print(find_fibonacci_seq_rec(n))
    print(find_fibonacci_seq_form(n))
