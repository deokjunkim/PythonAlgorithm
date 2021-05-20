# List Method
# append()
people = ["버피","페이스"]
people.append("자일스")
print(people)
people[len(people):] = ["잰더"]
print(people)
# extend()
people = ["버피","페이스"]
people.extend("자일스")
print(people)
people += "월로"
print(people)
people += ["젠더"]
print(people)
people[len(people):] += "잰더"
print(people)
# insert()

# remove()

# del문

# index()

# count()

# sort()
# sort(reversed=true)
# reserve()
# [::-1]

# unpacking
L = [2,3,4]
print(*L[:-2])

a = [y for y in range(1900,1940) if y %4 ==0]
print(a)
c = [x for x in a if x%2 == 0]
print(c)

l = list(range(10,20))
print(l)

# x = 4
# print(1 << x)
# 000
# 0100 << 1000
# 8421    8
# x = 8
# 1000
# print(x & (x-1))
s = '안녕 세상!'
print(s[-1] + s[:-1])
print(s[::-1])