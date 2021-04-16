import random

def testinf_radnom():
    """ test 모듈 테스트 """
    values = [1,2,3,4]
    print(random.choice(values))
    print(random.choice(values))
    print(random.choice(values))
    print(random.sample(values,2))
    print(random.sample(values,3))

    """ values 리스트를 섞는다 """
    random.shuffle(values)
    print(values)

    """ 0~10 임의 정수를 정의한다"""
    print(random.randint(0, 10))
    print(random.randint(0, 10))

if __name__ == "__main__":
    testinf_radnom()