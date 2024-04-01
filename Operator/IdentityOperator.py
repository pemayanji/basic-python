# Identity Operator : used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location.

a=90
b=80
c=90
print(id(a))
print (id(c))
print(a is not b)
print(a is b)
print(a is c)

x=[1,2,3,4,5]
y=[1,2,3,4,5]
print(id(x))
print(id(y))
print(x is y)