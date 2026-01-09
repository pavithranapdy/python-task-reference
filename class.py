# class myClass:
#     user = "pavithran"   # attribute

#     def f1(self):            # method
#         print("working")

# # object craetion
# obj1 = myClass()
# print(obj1.user)   ## access
# obj1.f1()



class Student:
    def _init_(self, name, age):
        self.name = name   # instance variable
        self.age = age

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)

s1 = Student("Arun", 21)   # object creation (calls _init_)
s2 = Student("Priya", 20)

s1.display()
s2.display()