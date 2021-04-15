from fractions import Fraction

def rounding_floasts(number1, places):
    print(round(number1, places))
    return round(number1, places)

def floadt_to_fractions(number):
    print(Fraction(*number.as_integer_ratio()))
    return Fraction(*number.as_integer_ratio())

def get_denominator(number1, number2):
    """ 분모를 반환한다."""
    a = Fraction(number1, number2)
    print(a.denominator)
    return a.denominator

def get_numerator(number1, number2):
    """ 분자를 반환한다."""
    a = Fraction(number1, number2)
    print(a.numerator)
    return a.numerator

def test_testing_floats():
    number1 = 1.25
    number2 = 1
    number3 = -1
    number4 = 5/4
    number6 = 6
    assert(rounding_floasts(number1, number2) == 1.2)
    assert(rounding_floasts(number1*10, number3) == 10)
    assert(floadt_to_fractions(number1) == number4)
    assert(get_denominator(number2, number6) == number6)
    assert(get_numerator(number2, number6) == number2)
    print("테스트 통과!")

if __name__ == "__main__":
    test_testing_floats()