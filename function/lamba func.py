#lamda function-> the function without name. it is used for instant use and one time use.lamda keywors is used.

"""x = lambda a,b : a+b
sum= x(3,4)
print(sum)

y=lambda c,d : c*d
mul= y(4,4)
print(mul)"""

#Resursive function -> function calling itself again and again
def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
print(factorial(3))

#filter()
#map()
