a = int(input("Enter any number"))
even="{} is even"
odd="{} is odd"

if a%2==0:
    print(even.format(a))
else:
    print(odd.format(a))