a="My country name is Nepal."
b="I am studying  at Xavier College."
c=a+b
print(len(a))
print(a[-1])    #last character
print(a[19:24])
print(a.upper())
print(a.lower())
print(a.replace("Nepal","America"))
print(a.split(" "))
print(c)

#Format() method

quantity= 5
item_no=957
price=43.33
myorder="I want to pay {} dollars for {} pieces of item_no {}"
print(myorder.format(price,quantity,item_no))