class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return 'Person: ' + self.name + ', ' + str(self.age)

    def print_name(self):
        print('Hello, my name is ' + self.name)

