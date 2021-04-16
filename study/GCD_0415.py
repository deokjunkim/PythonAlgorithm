def fiding_gcd(n,m):
    while m != 0:
        result = m
        n, m = n, n % m
    return result

def test_fiding_gcd():
    n = 12
    m = 21
    if(n > m):
        assert (fiding_gcd(n, m) == 3)
    else:
        assert (fiding_gcd(m, n) == 3)
    print('테스트 통과!')

if __name__ == "__main__":
    test_fiding_gcd()



