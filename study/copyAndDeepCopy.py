
# List Copy
myList = [1,2,3,4]

newList = myList[:]

newList2 = list(newList)

# Set Copy
people = {"버피","에인절","자일스"}
slayears = people.copy()
slayears.discard("자일스")
slayears.remove("에인절")

print(people)
print(slayears)

# Dict Copy

myDict = {"hi":"안녕"}
newDict = myDict.copy()

# Deep Copy
import copy
myObject = "다른 어떤 객체"

newObject = copy.copy(myObject) # 얕은 복사
newObject2 = copy.deepcopy(myObject) # 깊은 복사
myObject = "" #myObject[-1:]
print(newObject)
print(newObject2)
print(myObject)




