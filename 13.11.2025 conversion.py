# implicit
x = 10
y = 12.4
print(x,"+",y,"= ",x+y, type(x + y))

## explicit
a = input("Enter any positive value : ")# values are store in Str type
b = input("Enter any positive value : ")# values are store in Str type
print(a, type(a), b, type(b))

##### str to int
X = int(a)# str type to int type
Y = int(b)# str type to int type
print(X,"+",Y,"= ",X+Y, type(X + Y))

## int to str
firtstValue = str(X)#  change int to str
secondValue = str(Y)# change int to str
print(firtstValue,"+",secondValue,"= ",firtstValue+secondValue, type(firtstValue + secondValue))


active = True
change = str(active)# change bool to str
print(change,type(change))
valueofchange = int(active)# change bool to int
print(valueofchange,type(valueofchange))

### list to tuple
Block_A = ['Class A, Class B, Class C']# list
tupletypeBlock_A = tuple(Block_A)#change list to tuple
print(Block_A,type(Block_A),"to",tupletypeBlock_A,type(tupletypeBlock_A))

### tuple to list
DD=(10,20,30,40)#tuple
listDD=list(DD)#change tuple to list
print(DD,type(DD),"to",listDD,type(listDD))


