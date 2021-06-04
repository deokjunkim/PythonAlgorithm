def convert(number, base):
    convertString  = "01234567789ABCDEF"
    if number < base:
        return convertString[number]
    else:
        return convert(number // base, base) + convertString[number % base]

def test():
    number = 9
    base = 2
    assert(convert(number, base) == "1001")
    print("테스트 통과!")


if __name__ == "__main__":
    test()