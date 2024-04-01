fb="{} does not satisfy any condition"

for i in range(1,11):
    if (i%3==0) and (i%5==0):
        print("Fizzbuzz",i)
    elif (i%3==0):
        print("Fizz",i)
    elif (i%5==0):
        print("Buzz",i)
    else:
        print(fb.format(i))