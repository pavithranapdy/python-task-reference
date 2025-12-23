import mod1             #User defined Module or loads the module

# mod1 _ user created file in local folder or module
mod1.testingFun()       #calls a function, i.e., defined inside mod1.py
print(mod1.secretKey)   # print value of variable i.e., defined inside mod1.py 

# as m1 means imports the module(mod1) with short name(m1)
import mod1 as m1
m1.testingFun()         #calls a function from the module i.e., m1
myList = [10, 20, 30, 40]
m1.listData(myList)     #sends the list to a function in the module