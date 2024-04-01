# map(function,iterable)

def square(x):
    return x*x
numbers=[1,2,3]
square_number = map(square, numbers)
result=list(square_number)
print("Sqaure numbers are:",result)

# filter(function, iterable)

def is_even(x):
    return x % 2==0
numbers = [1,2,3,4,5,6,7,8,9,10]
even_number = filter(is_even, numbers)
result = tuple(even_number)
print("Even numbers are:",result)

def is_odd(x):
    return x % 2!=0
numbers = [1,2,3,4,5,6,7,8,9,10]
odd_number = filter(is_odd, numbers)
result = tuple(odd_number)
print("Odd numbers are:",result)
