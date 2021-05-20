# t1 = 1234, "안녕!"
# print(t1)

# t2 = t1, (1,2,3,4,5)
# print(t2)

# empty =()
# t1 = '안녕',
# print(len(empty))
# print(len(t1))
# t2 = '안녕!'
# print(t2)

# tuple method count(), index()
# t = 1,2,3,4,5,6,7,8,6,5,4,3,2,1
# print(t.count(1))
# print(t.index(2))
#
# # tuple unpacking
#
# x, *y = (1,2,3,5)
# print(x)
# print(y)
#
# *x, y = (1,2,3,4)
# print(x)
# print(y)

# named tuple
import collections
Person = collections.namedtuple('Person',['Name', 'Age', 'Gender'])
p = Person('김덕준','28','M')
print(p)
print(p.Name)
print(p.Age)
# p.Age = 25 This Not Able