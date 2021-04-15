def conver_to_decimal(number, base):
    multiplier, result = 1, 0
    while number > 0 :
        print('result : %d + (%d %% 10 * %d) = %d' % (result, number, multiplier, result + (number % 10 * multiplier)))
        result += number % 10 * multiplier

        print('multiplier : %d * %d = %d' % (multiplier, base, multiplier * base))
        multiplier *= base

        print('number : %d // 10 = %d' % (number, number // 10))
        number = number // 10

        print()
    return result

def conver_from_decimal(number, base):
    multiplier, result = 1, 0
    while number > 0 :
        print('%d + (%d %% %d * %d)' % (result, number, base, multiplier))
        result += number % base * multiplier
        print('result : %d'%result)

        print('%d * 10' % multiplier)
        multiplier *= 10
        print('multiplier : %d'%multiplier)

        print('%d // %d' % (number, base))
        number = number // base
        print('number : %d'%number)

        print()
    return result

def convert_from_decimal_larger_bases(number, base):
    strings = "0123456789ABCDEFGHIJ"
    result = ""
    while number > 0:
        digit = number % base
        result = strings[digit] + result
        number = number // base
    return result

def conver_dec_to_any_base_rec(number, base):
    convertString = "0123456789ABCEDEF"
    if number < base:
        return convertString[number]
    else:
        return conver_dec_to_any_base_rec(number // base, base) \
               + convertString[number % base]

def test_convert_to_decimal():
    number, base = 1001, 2
    # conver_to_decimal(number, base)
    number, base = 9, 2
    # conver_from_decimal(number, base)
    # assert(conver_to_decimal(number, base) == 9)
    assert(conver_dec_to_any_base_rec(number, base)=="1001")
    print("테스트 통과!")

if __name__ == "__main__":
    test_convert_to_decimal()
    # f = 100
    # ff = 102
    # print('%d * %d'%(f,ff))