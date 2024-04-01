l=float(input("Enter a length: "))
b=float(input("Enter a breadth: "))

def area():
    #local variable -> that is defines inside the function and cannot accessible from outside the function. Its scope is only around the declared function.
    global area_of_object
    area_of_object = l*b 
    return area_of_object

def volume():
    h=float(input("Enter a height: "))
    v=area_of_object*h
    return v
result=area()
result_volume=volume()
print(result)
print(result_volume)
