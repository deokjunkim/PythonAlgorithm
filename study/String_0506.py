# 유니코드 문자열
print(u'잘가\u0020세상')

#문자열 메소드 (join, reversed)
slayer = ["버피","앤","아스"]
print(" ".join(slayer))
print("-<ㅇ>-".join(slayer))
print("".join(slayer))
print("".join(reversed(slayer)))

#문자여 메소드(ljust, rjust)
name ="스칼렛"
print(name.ljust(10,"-"))
print(name.rjust(10,"_"))

# format
print("{0},{1}".format("안녕","파이썬"))
print("이름 : {who}, 나이 : {age} ".format(who="제임스",age="28"))
print("{0}은 나이가 {age}살 입니다".format("고든",age="12"))

# 문자열 : !s, 표현 : !r, 아스키코 : !a
import decimal
print("{0} {0!s} {0!r} {0!a}".format(decimal.Decimal("99.9")))

#문자열 언팩킹 **locals()
hero = "버피"
number = 999
print("{number}, {hero}".format(**locals()))
print(locals())

#splitline()
slayer = "로미오\n줄리엣"
print(slayer.splitlines())

#split() 메소드
start = "안녕*세상*!"
print(start.split("*",1))
print(start.rsplit("*",1))

#strip() 문자열 앞 뒤 제거
slayer = "999로미오999 & 999줄리엣 999"
print(slayer.strip("999"))

import string
import sys

def count_unique_word():
    words = {}
    strip = string.whitespace + string.punctuation + string.digits + "\""
    print(strip)
    for filename in sys.argv[1:]:
        with open(filename) as file:
            for line in file:
                for word in line.lower().split():
                    word = word.strip(strip)
                    if len(word) > 2:
                        words[word] = words.get(word,0) + 1

    for word in sorted(words):
        print("{0}: {1}번".format(word,words[word]))

if __name__ == "__main__":
    count_unique_word()
