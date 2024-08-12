

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

p1 = Person('John', 25)
print(p1.get_name(), p1.get_age())

class Employee(Person):
    def __init__(self, name, age, id):
        super().__init__(name, age)
        self.id = id
    def get_id(self):
        return self.id
e1 = Employee('Jack', 25, 'Jack4321')
print(e1.get_name(), e1.get_age(), e1.get_id())

