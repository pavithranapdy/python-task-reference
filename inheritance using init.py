print("Single inheritance in __init__")
class Parent:
    def __init__(self, name):
        self.name = name
        print("Parent constructor")
    def show_parent(self):
        print("Parent name:", self.name)

class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)   # call Parent's __init__
        self.age = age
        print("Child constructor")
    def show_child(self):
        print("Child age:", self.age)

obj = Child("Alice", 20)
print("input name",obj.name, obj.age)
obj.show_parent()
obj.show_child()