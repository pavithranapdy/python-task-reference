# # single inheritance -One child class inherits from one parent class.
# print("Single inheritance")
# class Parent:
#     def show(self):
#         print("This is Parent class")

# class Child(Parent):
#     def display(self):
#         print("This is Child class\n")

# obj = Child()
# obj.show()
# obj.display()
## using __init__
# class Parent:
#     def __init__(self, name, age):
#         self.name = name   # Parent class variable
#         self.age = age  # Parent class variable

# class Child(Parent):
#     def __init__(self, name, age):
#         super().__init__(name,age)   # Access Parent constructor
#         self.Name = "Demo"
#         self.Age = 20          # Child class variable

#     def display(self):
#         print("parent Name:", self.name)
#         print("parentAge:", self.age)
#         print("child Name:", self.Name)
#         print("child Age:", self.Age)

# obj = Child("Arun", 39)
# obj.display()



#
# # multiple inheritance
# print("Multiple inheritance")
# class Father:
#     def f(self):
#         print("Father class is working")

# class Mother:
#     def m(self):
#         print("Mother class is working\n")

# class Child(Father, Mother):
#     pass

# obj = Child()
# obj.f()
# obj.m()



# # multilevel inheritance
# print("Multilevel inheritance")
# class Grandparent:
#     def gp(self):
#         print("Grandparent class")

# class Parent(Grandparent):
#     def p(self):
#         print("Parent class")

# class Child(Parent):
#     def c(self):
#         print("Child class")

# obj = Child()
# obj.gp()
# obj.p()
# obj.c()



# # Hierarchical Inheritance
# print("Hierarchical inheritance")
# class parent():
#     motherName = "mother"

# class Child1(parent):
#     child1Name = "child1"

# class Child2(parent):
#     child2Name = "child 2"

# obj = Child1()
# obj2 = Child2()
# print(obj.motherName)
# print(obj2.motherName)
# print(obj2.child2Name)


# # hybrid inheritance
# print("hybrid inheritance")
# class A:
#     def a(self):
#         print("Class A")

# class B(A):
#     def b(self):
#         print("Class B")

# class C(A):
#     def c(self):
#         print("Class C")

# class D(B, C):
#     def d(self):
#         print("Class D\n")

# obj = D()
# obj.a()
# obj.b()
# obj.c()
# obj.d()