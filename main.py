from person import Person

if 5 > 2:
    print('5 is greater than 2')

# This is a comment
y = 'Hello, World!'
print(y)

x = str('Hello')
print(type(x))
print(len(x))

x = bool(0)
print(x)

new_list = ['apple', 'banana', 'cherry']
print(new_list)
print(new_list[1])
print(len(new_list))
for x in new_list:
    print(x)

fruits_with_a = []
for x in new_list:
    if 'a' in x:
        fruits_with_a.append(x)

print(fruits_with_a)

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse=True)
print(thislist)

thislist = thislist + new_list
print(thislist)

class MyClass:
    x = 5
o = MyClass()
print(o.x)


p1 = Person('John', 36)
print(p1)

def can_vote(age):
    if age >= 18:
        return True
    else:
        return False

print(can_vote(p1.age))
p1.print_name()

class Student(Person):
    def __init__(self, name, age, year):
        super().__init__(name, age)
        self.graduation_year = year

    def welcome(self):
        print('Welcome', self.name, 'to the class of', self.graduation_year)

s1 = Student('Mike', 22, 2025)
s1.welcome()
